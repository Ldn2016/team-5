import requests
import json
import re

isbn_lookup_base = "https://www.googleapis.com/books/v1/volumes?q=isbn:"


#todo: include get_book_data() from Phoebe
def get_book_data(isbn):
    #isbn inputted as string
    address = isbn_lookup_base + isbn
    r = requests.get(address)
    data = json.loads(r.text)
    info_to_return = {}
    given_info = data.get("data")[0]
    info_to_return["author"] = given_info.get("volumeInfo").get("title")
    info_to_return["title"] = given_info.get("volumeInfo").get("authors")
    info_to_return["imglink"] = given_info.get("imageLinks").get("thumbnail")
    return (info_to_return)

def create_author_string(authors: list): -> str
    author_string = ""
    for author in authors:
        author_string = author_string + author + ", "
    author_string = author_string[:-2]
    return author_string
    
def get_generic_product_data(barcode):
    url = "http://opengtindb.org/index.php?cmd=ean1&ean=" + barcode + "&sq=1"
    print(url)
    r = requests.get(url)
    
    text = r.text
    data = re.findall('NAME=\"fullname\" VALUE=\"(.*?)\">', text, re.DOTALL)
    if len(data) > 0:
        return data[0]
    else:
        return None


print(get_generic_product_data("7622300743536"))


#if is_isbn(barcode):
#    data = get_book_data(barcode)
#    #do any processing necessary
#    return data
  
#else:
#    data = get_generic_product_data(barcode)
#    #do some processing
#    return data

def is_isbn(isbn):
    if (len(isbn) != 10) and (len(isbn) != 13):
        #print(len(isbn))
        return False
    if len(isbn) == 13:
        sum = 0
        for i in range(0, 12):
            digit = int(isbn[i])
            if (i % 2 == 1):
                sum += 3 * digit
            else:
                sum += digit
        check = (10 - (sum % 10)) % 10
        #print("Check digit is ", check)
        return (check == int(isbn[len(isbn) - 1]))
    if len(isbn) == 10:
        sum = 0
        weight = 10
        for i in range(0,8):
            digit = int(isbn[i])
            sum += weight * digit
            weight = weight - 1
        check = 11 - (sum % 11)
        if check == 10:
            check = 'X'
        return (check == isbn[len(isbn) - 1])


