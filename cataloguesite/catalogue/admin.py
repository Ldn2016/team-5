from django.contrib import admin
from .models import Book, Store, Quantity

admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Quantity)
