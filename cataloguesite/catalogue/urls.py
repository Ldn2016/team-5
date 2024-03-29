from django.conf.urls import url
from . import views

"Matches the urls on the website to python scripts at views.py"

urlpatterns = [
        url(r'^store/(?P<store_id>[0-9]+)/$', views.store_detail, name='store_detail'), #Matches store id and number to a webpage showing the details of a store.
        url(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'), #Matches book id and number to a webpage showing the details of a book.
        url(r'^storelist/$', views.store_list, name='store_list'),
        url(r'^search/$', views.search, name='search'),
        url(r'^search_by_title/$', views.search_by_title, name='search_by_title'),
        url(r'^bookpost/$', views.book_post, name='book_post'),
        url(r'^scanner/$', views.barcode_scanner, name='barcode_scanner'),
        url(r'^product_enter/$', views.product_enter, name='product_enter'),
        url(r'^contact/$', views.contact_page, name='contact_page'),
        ]