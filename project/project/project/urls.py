from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('area-riservata/', admin.site.urls),
    path('', include('sections.urls')),
]
