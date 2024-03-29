from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse 
from .models import Book, Store, Quantity
import requests
import json
import re

"""This page stores how Django processes the input on each webpage"""

isbn_lookup_base = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

@csrf_exempt
def book_post(request):
    "Takes the POST data from the scanner page and puts the data on the confirmation page"
    try:
        print(request.POST)
        data = get_book_data(request.POST['isbn'])
        data['store'] = request.POST['store']
        return render(request, 'catalogue/product_scan_check.html', {'info' : data})
    except KeyError:
        return render(request, 'catalogue/product_scanner.html')

def get_book_data(isbn):
    "Looks up the ISBN on the Google API and returns the title, author and thumbnail"
    #isbn inputted as string
    address = isbn_lookup_base + isbn
    r = requests.get(address)
    data = json.loads(r.text)
    info_to_return = {}
    info_to_return["isbn"] = isbn
    info_to_return["title"] = data['items'][0]['volumeInfo']['title']
    info_to_return["author"] = data['items'][0]['volumeInfo']['authors'][0]
    info_to_return["thumbnail"] = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    return info_to_return

@csrf_exempt
def product_enter(request):
    "Submits the request to the database via POST"
    print(request.POST)
    book_title = request.POST['title']
    book_author = request.POST['author']
    book_isbn = request.POST['isbn']
    book_thumbnail = request.POST['thumbnail']
    book, _ = Book.objects.get_or_create(id_number=int(book_isbn), title=book_title, author=book_author, thumbnail=book_thumbnail)
    store, _ = Store.objects.get_or_create(name=request.POST['store'])
    quantity, _ = Quantity.objects.get_or_create(store=store, item=book,
                                                 defaults={"amount": 0})
    quantity.amount += 1
    quantity.save()
    return render(request, 'catalogue/thank_you.html')


def book_detail(request, book_id):
    """
    Get detail for a specific book.
    """
    book = get_object_or_404(Book, id_number=book_id)
    records = Quantity.objects.filter(item__pk=book_id)
    stores = [r.store for r in records if r.amount > 0]
    return render(request, 'catalogue/book_detail.html', {'book': book,
                                                          'stores': stores})


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
    "Returns search form"
    return render(request, 'catalogue/search.html')


def barcode_scanner(request):
    "Takes user to page where they can scan in a product."
    return render(request, 'catalogue/product_scanner.html')

def contact_page(request):
    "Returns contact page"
    return render(request, 'catalogue/contact_page.html')


def search_by_title(request):
    """Performs search function - takes the query on the form on a search page (via get request) and returns a page
    which displays books whose titles contain the search request. """
    query = request.GET.get('q', '')
    results = Book.objects.filter(title__contains = query)
    return render(request, 'catalogue/search_results.html', {'results' : results})                       

