from django.urls import include, path

from . import views
from .feed import SectionRssSiteNewsFeed, SectionAtomSiteNewsFeed

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pubblicazioni/', include([
        path('elenco-completo/', views.all_posts, name='all_posts'),
        path('risultati/', views.search, name='search_results'),
        path('<slug:slug_category>/', views.single_category, name='single_category'),
        path('<slug:slug_category>/feed/', SectionRssSiteNewsFeed(), name='section_feed'),
        path('<slug:slug_category>/atom/', SectionAtomSiteNewsFeed(), name='section_atom'),
        path('<slug:slug_category>/<slug:slug_post>/', views.single_post, name='single_article'),
    ])),
]