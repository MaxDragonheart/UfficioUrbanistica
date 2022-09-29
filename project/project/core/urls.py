from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticSitemap, FlatpageSitemap

sitemap_elements = {
    'staticpages': StaticSitemap,
    'flatpages': FlatpageSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemap_elements}, name='sitemap'),

    path('', include('sections.urls')),
    path('utenti/', include('usermanager.urls')),
    path('open-geodata/', include('opengeodata.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
