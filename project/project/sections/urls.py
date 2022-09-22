from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.tmp_homepage, name='temporary_homepage'),
    path('', views.homepage, name='homepage'),
    path('<slug:slug_category>/', views.single_category, name='single_category'),
    path('pubblicazioni/<slug:slug_category>/<slug:slug_post>/', views.single_post, name='single_article'),
]