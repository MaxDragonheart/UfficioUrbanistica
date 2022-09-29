import datetime
from pathlib import Path

from django.conf import settings
from django.contrib.gis.db import models
from django.template.context_processors import request
from django.urls import reverse

from abstracts.models import TimeManager, ModelPost, CategoryBase
from core.models import SiteCustomization
from fsspec import get_fs_token_paths

from .utils import get_wms_bbox, get_centroid_coords, get_wms_thumbnail, WMS_THUMBNAILS


class OpenLayersMapParameters(models.Model):
    """
    OpenLayersMapParameters Abstract Model define the map's parameters based on
    OpenLayers [Map object](https://openlayers.org/en/latest/apidoc/module-ol_Map-Map.html).
    """
    map_scaleline = models.BooleanField(default=True)
    map_center_longitude = models.DecimalField(max_digits=10, decimal_places=5, default=14.23964)
    map_center_latitude = models.DecimalField(max_digits=10, decimal_places=5, default=40.84290)
    set_max_zoom = models.IntegerField(default=28)
    set_min_zoom = models.IntegerField(default=0)
    set_zoom_level = models.IntegerField(default=0)

    class Meta:
        abstract = True


class GeoServerDomain(TimeManager):
    """
    GeoServerDomain Model inherits TimeManager, it is useful to
    create a Geoserver's domain object.
    e.g.:
        geoserver_domain='www.mygeoserver.me'
        geoserver_workspace='MyWorkSpace'

        Geoserver URL: 'www.mygeoserver.me/geoserver/MyWorkSpace'
        WMS: 'www.mygeoserver.me/geoserver/MyWorkSpace/wms'
        WFS: 'www.mygeoserver.me/geoserver/MyWorkSpace/wfs'
    """
    domain = models.URLField(unique=True)

    def __str__(self):
        return self.domain

    class Meta:
        ordering = ['domain']
        verbose_name = "Geoserver Domain"
        verbose_name_plural = "Geoserver Domains"


class GeoserverWorkspace(TimeManager):
    """
    GeoserverWorkspace Model inherits TimeManager, it is useful to
    create a Geoserver's Workspace object.
    """
    workspace = models.CharField(max_length=100)

    def __str__(self):
        return self.workspace

    class Meta:
        ordering = ['workspace']
        verbose_name = "Geoserver Workspace"
        verbose_name_plural = "Geoserver Workspaces"


class Categories(CategoryBase):
    def get_absolute_url(self):
        return reverse("category-single", kwargs={"slug_category": self.slug_category})

    class Meta:
        ordering = ['category_name']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"


class OGCLayer(ModelPost, OpenLayersMapParameters):
    """
    OGCLayer Model inherits from BaseModelPost and OpenLayersMapParameters. This
    model can build an OGC layer using the attributes from OpenLayers [Layer objectc](https://openlayers.org/en/latest/apidoc/module-ol_layer_Layer-Layer.html).
    """
    geoserver_domain = models.ForeignKey(GeoServerDomain, on_delete=models.PROTECT, related_name="related_geoserverdomain")
    geoserver_workspace = models.ForeignKey(GeoserverWorkspace, on_delete=models.PROTECT, related_name="related_geoserverworkspace")
    categories = models.ManyToManyField(Categories, related_name="related_ogclayer_categories")

    set_zindex = models.IntegerField(default=1)
    set_opacity = models.DecimalField(max_digits=3, decimal_places=2, default=1.0)
    ogc_layer_name = models.CharField(max_length=100)
    ogc_layer_style = models.CharField(max_length=100, blank=True, null=True)
    ogc_bbox = models.CharField(max_length=250, blank=True, null=True)
    ogc_centroid = models.CharField(max_length=250, blank=True, null=True)
    ogc_legend = models.BooleanField(default=False)
    is_vector = models.BooleanField(default=False)
    is_raster = models.BooleanField(default=False)

    @property
    def complete_url_wms(self):
        return f"{self.geoserver_domain.domain}/geoserver/{self.geoserver_workspace.workspace}/wms"

    @property
    def complete_url_wfs_wcs(self):
        if self.is_vector:
            url = f"{self.geoserver_domain.domain}/geoserver/{self.geoserver_workspace.workspace}/wfs"
        elif self.is_raster:
            url = f"{self.geoserver_domain.domain}/geoserver/{self.geoserver_workspace.workspace}/wcs"
        else:
            url = "Set if is vector or raster!"

        return url

    def get_absolute_url(self):
        return reverse("layer-single", kwargs={"slug_post": self.slug_post})

    def save(self, *args, **kwargs):
        """Override save method and add to DB thumbnail path, BBOX and centroid.

        Args:
            *args:
            **kwargs:
        """
        # Create the thumbnail destination folder
        today = datetime.datetime.now()
        today_folder = Path(f"{today.year}/{today.month}/{today.day}")
        output_folder = settings.MEDIA_FOLDER / WMS_THUMBNAILS
        destination_folder = output_folder / today_folder
        fs, fs_token, paths = get_fs_token_paths(destination_folder)
        fs.mkdirs(path=destination_folder, exist_ok=True)

        # Get thumbnail from WMS
        img_path = get_wms_thumbnail(
            wms_url=self.complete_url_wms,
            service_version="1.3.0",
            layer_name=self.ogc_layer_name,
            output_data_folder=destination_folder,
        )
        self.header_image = f"{WMS_THUMBNAILS}/{today_folder}/{img_path.stem}{img_path.suffix}"

        # Get WMS's BBOX
        self.ogc_bbox = list(get_wms_bbox(
            wms_url=self.complete_url_wms,
            service_version="1.3.0",
            layer_name=self.ogc_layer_name
        ))

        # Get BBOX's centroid
        self.ogc_centroid = list(get_centroid_coords(self.ogc_bbox))

        # Save all
        super(OGCLayer, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "OGC Layer"
        verbose_name_plural = "OGC Layers"


class WebGISProjectBase(ModelPost, OpenLayersMapParameters):
    """
    WebGISProjectBase Abstract Model collect ModelPost and OpenLayersMapParameters.
    """

    class Meta:
        abstract = True


class WebGISProject(WebGISProjectBase):
    """
    WebGISProject Model inherits WebGISProjectBase, it is useful to create a webgis.
    """
    categories = models.ManyToManyField(Categories, related_name="related_webgisproject_categories")
    main_layer = models.ForeignKey(OGCLayer, on_delete=models.PROTECT, related_name="related_main_wmslayer")
    layers = models.ManyToManyField(OGCLayer, related_name="related_wmslayers", blank=True)

    def get_absolute_url(self):
        return reverse("webgis-single", kwargs={"slug_post": self.slug_post})

    @property
    def meta_image(self):
        if self.header_image:
            meta_image = self.header_image
        else:
            meta_image = SiteCustomization.objects.get(id=1).header_image
        return meta_image

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "WebGIS"
        verbose_name_plural = "WebGIS"
