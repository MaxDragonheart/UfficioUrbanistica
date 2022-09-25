from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(f'{settings.ADMIN_PANEL_ROOT}/', include([
        path('', admin.site.urls),
        path('tinymce/', include('tinymce.urls')),
    ])),
    path('', include('core.urls')),
]
