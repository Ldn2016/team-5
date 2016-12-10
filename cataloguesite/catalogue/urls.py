from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^store/(?P<store_id>[0-9]+)/$', views.store_detail, name='store_detail'),
        url(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
]
