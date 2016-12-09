import requests
import json

#todo: include get_book_data from Phoebe

def get_generic_product_data(barcode)
    r = requests.get("https://www.buycott.com/upc/%s/" % barcode)
    text = r.text


print(get_generic_product
if is_isbn(barcode):
    data = get_book_data(barcode)
    #do any processing necessary
    return data
else:
    data = get_generic_product_data(barcode)
    #do some processing
    return data

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


