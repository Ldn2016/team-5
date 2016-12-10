from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse 
from .models import Book, Store, Quantity
import requests
import json
import re

isbn_lookup_base = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

def get_book_data(isbn):
    #isbn inputted as string
    address = isbn_lookup_base + isbn
    r = requests.get(address)
    data = json.loads(r.text)
    info_to_return = {}
    info_to_return["isbn"] = isbn
    info_to_return["title"] = data['items'][0]['volumeInfo']['title']
    info_to_return["author"] = data['items'][0]['volumeInfo']['authors'][0]
    return info_to_return

def product_enter(request):
    book_isbn = request.POST['info.isbn']
    book_title = request.POST['info.title']
    book_author = request.POST['info.author']
    new_book = Book(id_number = int(book_isbn), title = book_title, author = book_author)
    

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

    stores = Store.objects.all()
    return render(request, 'catalogue/store_list.html', {'stores': stores})


def store_detail(request, store_id):
    """
    List the books in store at a store.
    """
    store = Store.objects.get(pk=store_id)
    records = Quantity.objects.filter(store__pk=store_id)
    books = [(r.item, r.amount) for r in records if r.amount > 0]
    return render(request, 'catalogue/store_detail.html', {'books': books,
                                                           'store': store, })


def search(request):
    return render(request, 'catalogue/search.html')


def barcode_scanner(request):
    return render(request, 'catalogue/product_scanner.html')

@csrf_exempt
def book_post(request):
    print(request.POST)
    data = get_book_data(request.POST['isbn'])
    return render(request, 'catalogue/product_scan_check.html', {'info' : data})


def search_by_title(request):
    query = request.GET.get('q', '')
    results = Book.objects.filter(title__contains = query)
    return render(request, 'catalogue/search_results.html', {'results' : results})                       

