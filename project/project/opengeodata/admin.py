from django.contrib import admin

from .models import GeoServerDomain, GeoserverWorkspace, OGCLayer, WebGISProject, Categories


class GeoServerDomainAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["domain"]}),
    ]

    class Meta:
        model = GeoServerDomain


class GeoserverWorkspaceDomainAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["workspace"]}),
    ]

    class Meta:
        model = GeoserverWorkspace


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_category": ("category_name",)}
    fieldsets = [
                (None, {"fields": ["category_name", "slug_category"]}),
            ]

    class Meta:
        model = Categories


class OGCLayerAdmin(admin.ModelAdmin):
    list_display = ["title", "ogc_layer_name", "publishing_date", "ogc_bbox", "ogc_centroid", "complete_url_wms", "complete_url_wfs_wcs", "header_image"]
    list_filter = ["publishing_date"]
    search_fields = ["title"]
    prepopulated_fields = {"slug_post": ("title",)}
    fieldsets = [
                ("Meta description", {"fields": ["title", "slug_post", "description", "contents", "categories", "draft"]}),
                ("Geoserver", {"fields": ["geoserver_domain", "geoserver_workspace"]}),
                ("OGC Parameters", {"fields": [
                    "ogc_layer_name", "ogc_layer_style", "ogc_legend", "is_vector", "is_raster",
                ]}),
                ("OpenLayers Parameters",
                 {"fields": ["set_max_zoom", "set_min_zoom", "set_zindex", "set_opacity"]}
                 ),
            ]

    class Meta:
        model = OGCLayer


class WebGISProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "publishing_date", "updating_date", "highlighted", "draft"]
    list_filter = ["publishing_date"]
    search_fields = ["title"]
    prepopulated_fields = {"slug_post": ("title",)}
    fieldsets = [
                ("Meta description", {"fields": ["title", "slug_post", "header_image", "description"]}),
                ("Contents", {"fields": ["contents", "categories"]}),
                ("Options", {"fields": ["draft", "highlighted", "publishing_date"]}),
                ("OpenLayers Parameters",
                 {
                     "classes": ("collapse",),
                     "fields":
                      ["map_scaleline", "map_center_longitude", "map_center_latitude", "set_max_zoom", "set_min_zoom",
                       "set_zoom_level"
                       ]
                  }
                 ),
                ("OGC Layer",  {"fields": ["main_layer", "layers"]}),
            ]

    class Meta:
        model = WebGISProject


admin.site.register(GeoServerDomain, GeoServerDomainAdmin)
admin.site.register(GeoserverWorkspace, GeoserverWorkspaceDomainAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(OGCLayer, OGCLayerAdmin)
admin.site.register(WebGISProject, WebGISProjectAdmin)
