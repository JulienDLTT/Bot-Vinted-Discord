from pyVinted import Vinted
from time import sleep
import webbrowser

vinted = Vinted()
# search(url, number_of_items, page_number)
#returns a list of objects: item
test = 1

while True:
    items = vinted.items.search("https://www.vinted.fr/catalog?brand_ids[]=53&order=newest_first&price_to=30&currency=EUR",10,1)
    for i in range(9):
        item1 = items[i]
        if item1.brand_title == 'Nike':
            objet = item1.title
            print(objet)
            objet = item1.url
            webbrowser.open(objet)
            print(objet)
            objet = item1.brand_title
            print(objet)

    sleep(0.3)
    print("nike fait")

    items = vinted.items.search("https://www.vinted.fr/catalog?currency=EUR&price_to=30&order=newest_first&brand_ids[]=88&brand_ids[]=430791&brand_ids[]=4559748&brand_ids[]=6962946",10,1)
    for i in range(9):
        item1 = items[i]
        if item1.brand_title == 'Ralph Lauren' or item1.brand_title == 'Lauren Ralph Lauren' or item1.brand_title == 'RALPH Ralph Lauren' or item1.brand_title == 'Ralph Lauren Sport' :
            objet = item1.title
            print(objet)
            objet = item1.url
            webbrowser.open(objet)
            print(objet)
            objet = item1.brand_title
            print(objet)

    sleep(0.3)
    print("ralph fait")

    items = vinted.items.search("https://www.vinted.fr/catalog?price_to=30&currency=EUR&order=newest_first&brand_ids[]=362&brand_ids[]=872289",10,1)
    for i in range(9):
        item1 = items[i]
        if item1.brand_title == 'Carhartt' or item1.brand_title == 'Carhartt WIP':
            objet = item1.title
            print(objet)
            objet = item1.url
            webbrowser.open(objet)
            print(objet)
            objet = item1.brand_title
            print(objet)

    sleep(0.3)
    print("carharrt fait")
    print(test)
    test = test + 1
    i = 1