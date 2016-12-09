from django.contrib import admin
from .models import Item, Book, CD, Store, Quantity

admin.site.register(Item)
admin.site.register(Book)
admin.site.register(CD)
admin.site.register(Store)
admin.site.register(Quantity)
