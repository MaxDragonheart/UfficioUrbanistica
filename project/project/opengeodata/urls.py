from django.urls import path, include

from . import views
from .feed import CategoriesAtomSiteNewsFeed, CategoriesRssSiteNewsFeed

urlpatterns = [
    path('', views.opengeodata, name='open-geodata'),
    path('risultati/', views.search, name='open-geodata-search'),
    path('categorie/<slug:slug_category>/', views.single_category, name='category-single'),
    path('categorie/<slug:slug_category>/feed/', CategoriesRssSiteNewsFeed(), name='category_feed'),
    path('categorie/<slug:slug_category>/atom/', CategoriesAtomSiteNewsFeed(), name='category_atom'),
    path('wms/', include([
        path('<slug:slug_post>/', views.single_wms, name='layer-single'),
    ])),
    path('webgis/', include([
        path('<slug:slug_post>/', views.single_webgis, name='webgis-single'),
    ])),
]