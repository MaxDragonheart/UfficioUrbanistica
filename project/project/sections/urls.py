from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.tmp_homepage, name='temporary_homepage'),
    path('<slug:slug_category>/', views.single_category, name='single_section'),
]