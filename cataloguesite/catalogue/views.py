from django.shortcuts import render
from .models import CD, Book, Store, Quantity


def add_item(item_dict):
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
    Add an item to the directory.
    `item_dict` should be a Python dict, not JSON.
    """
    models_dict = {"book": Book, "cd": CD, }
    new_item, _ = models_dict[item_dict["type"]].objects.get_or_create(**item_dict["object"])
    store, _ = Store.objects.get_or_create(name=item_dict["store"])
    quantity, _ = Quantity.objects.get_or_create(item=new_item, store=store,
                                                 defaults={"amount": 0})
    quantity.amount += 1
    quantity.save()


def index(request):
    pass
