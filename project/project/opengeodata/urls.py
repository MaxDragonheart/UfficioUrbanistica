from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.opengeodata, name='open-geodata'),
    path('category/<slug:slug_category>/', views.single_category, name='category-single'),
    path('wms/', include([
        # path('feed/', FeedOGCLayer(), name='wms-feed'),
        # path('atom/', AtomOGCLayer(), name='wms-atom'),
        path('', views.wms_list, name='layer-list'),
        path('<slug:slug_post>/', views.single_wms, name='layer-single'),
    ])),
    path('webgis/', include([
        # path('feed/', FeedWebGISProject(), name='map-feed'),
        # path('atom/', AtomWebGISProject(), name='map-atom'),
        path('', views.webgis_list, name='webgis-list'),
        path('<slug:slug_post>/', views.single_webgis, name='webgis-single'),
    ])),
]