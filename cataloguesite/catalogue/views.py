from django.shortcuts import render, get_object_or_404
from .models import Book, Store, Quantity


def add_item(item_dict):
    """
    Add JSON objects to the database in the correct way.

    JSON objects should be formatted as so:
        {
            "store": store,
            "amount": amount,
            "object": {
                "title": title,
                etc.
            }
        }
    Add an item to the directory.
    `item_dict` should be a Python dict, not JSON.
    """
    new_item, _ = Book.objects.get_or_create(**item_dict["object"])
    store, _ = Store.objects.get_or_create(name=item_dict["store"])
    quantity, _ = Quantity.objects.get_or_create(item=new_item, store=store,
                                                 defaults={"amount": 0})
    quantity.amount += 1
    quantity.save()


def book_detail(request, book_id):
    """
    Get detail for a specific book.
    """
    book = get_object_or_404(Book, id_number=book_id)
    return render(request, 'catalogue/book_detail.html', {'book': book})


def store_list(request):
    """
    List all the stores that exist.
    """
    pass


def store_detail(request, store_id):
    """
    List the books in store at a store.
    """
    for r in Quantity.objects.all():
        print(r.store.pk)
    records = Quantity.objects.filter(store__pk=store_id)
    print(len(records))
    books = [(r.book, r.amount) for r in records if r.amount > 0]
    return render(request, 'catalogue/store_detail.html', {'books': books})
