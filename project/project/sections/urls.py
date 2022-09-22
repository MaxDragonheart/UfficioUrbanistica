from django.urls import include, path

from . import views

urlpatterns = [
    # path('', views.tmp_homepage, name='temporary_homepage'),
    path('', views.homepage, name='homepage'),
    path('pubblicazioni/', include([
        path('elenco-completo/', views.all_posts, name='all_posts'),
        path('<slug:slug_category>/', views.single_category, name='single_category'),
        path('<slug:slug_category>/<slug:slug_post>/', views.single_post, name='single_article'),
    ])),
]