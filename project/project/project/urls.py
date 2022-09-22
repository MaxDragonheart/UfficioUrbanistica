from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(f'{settings.ADMIN_PANEL_ROOT}/', include([
        path('', admin.site.urls),
        path('tinymce/', include('tinymce.urls')),
    ])),
    path('', include('sections.urls')),
    path('user/', include('usermanager.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)