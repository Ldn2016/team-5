from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^store/(?P<store_id>[0-9]+)/$', views.store_detail, name='store_detail'),
        url(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
        url(r'^storelist/$', views.store_list, name='store_list'),
        url(r'^search/$', views.search, name='search'),
        url(r'^search_by_title/$', views.search_by_title, name='search_by_title'),

]
