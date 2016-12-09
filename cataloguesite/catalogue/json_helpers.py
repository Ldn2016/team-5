"""
Add JSON objects to the database in the correct way.

JSON objects should be formatted as so:
    {
    "type": object type,
    "store": store name,
    "object": {
              "id_number": id_number,
              etc.
              }
    }
"""
import os
import sys
sys.path.append(os.getcwd())
from django.conf import settings
settings.configure()
import django
django.setup()
import models


def add_item(item_dict):
    """
    Add an item to the directory.
    `item_dict` should be a Python dict, not JSON.
    """
    models_dict = {"book": models.Book, "cd": models.CD, }
    new_item, _ = models_dict[item_dict["type"]].objects.get_or_create(**item_dict["object"])
    store, _ = models.Store.objects.get_or_create(name=item_dict["store"])
    quantity, _ = models.Store.objects.get_or_create(item=new_item, store=store,
                                                     defaults={"amount": 0})
    quantity.amount += 1
    quantity.save()


if __name__ == "__main__":
    add_item({
             "type": "book",
             "store": "Oxf*rd",
             "object": {
                       "id_number": 666,
                       "title": "The city this book is in is bad.",
                       "author": "Mr Bad Author",
                       }
             })
