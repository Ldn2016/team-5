import requests
import json
import re


#todo: include get_book_data() from Phoebe
def get_book_data(isbn):
    #isbn inputted as string
    address = "http://isbndb.com/api/v2/json/NAZ4ZQZO/book/"+isbn
    r = requests.get(address)
    data = json.loads(r.text)
    info_to_return = {}
    given_info = data.get("data")[0]
    info_to_return["author"] = given_info.get("author_data")[0].get("name")
    info_to_return["title"] = given_info.get("title_latin")
    return (info_to_return)
    
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


