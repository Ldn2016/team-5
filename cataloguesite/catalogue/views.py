from django.shortcuts import render, get_object_or_404
from .models import Item, Store, Quantity


def add_item(item_dict):
    """
    Add JSON objects to the database in the correct way.

    JSON objects should be formatted as so:
        {
            "store": store,
            "amount": amount,
            "object": {
                "kind": book/CD/whatever,
                "title": title,
                etc.
            }
        }
    Add an item to the directory.
    `item_dict` should be a Python dict, not JSON.
    """
    new_item, _ = Item.objects.get_or_create(**item_dict["object"])
    store, _ = Store.objects.get_or_create(name=item_dict["store"])
    quantity, _ = Quantity.objects.get_or_create(item=new_item, store=store,
                                                 defaults={"amount": 0})
    quantity.amount += 1
    quantity.save()


def item_detail(request, item_id):
    """
    Get detail for a specific book.
    """
    item = get_object_or_404(Item, id_number=item_id)
    return render(request, 'catalogue/item_detail.html', {'item': item})

def store_list(request):
    """
    List all the stores that exist.
    """

