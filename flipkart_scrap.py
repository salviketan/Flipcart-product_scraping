from bs4 import BeautifulSoup as bs
import requests
import csv
import os

# *****Create empty list to save items. *****#
products = []
stars = []
prices = []


# *****Create User-Agent***** #
user_agent = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}


# *****Url of site which to be scrapped***** #
site =  "https://www.flipkart.com/search?q="


# *****Get search query from user***** #
search = input("Enter the Search query: ")

#pages_to_search=int(input("Please enter the pages to search : "))
#for i in range(pages_to_search):


# *****Create full Url***** #
url= site + search  #+ "&page={i}".format(i=i+1)
#    urls.append(page_url)
#print(urls)
#for url in urls:


# *****Make get request to url using requests library***** #
r=requests.get(url , headers = user_agent)


# *****Use BeautifulSoup to convert scrapped dato into text***** #
soup=bs(r.text , 'html5lib')


# *****Scrap data which is needed***** #
boxes=soup.find_all('div',class_='_1-2Iqu row')   # bhgxx2 col-12-12


# *****Logic to scrap needed product info***** #
for box in boxes:
    try:
        product_item=box.find('div',class_='_3wU53n')
        product_star=box.find('div',class_='hGSR34')
        product_price=box.find('div',class_='_1vC4OE _2rQ-NK')
        product=product_item.get_text()
        star=product_star.get_text()
        price=product_price.get_text()
        products.append(product)
        stars.append(star)
        prices.append('Rs. '+price.lstrip('₹'))  #You set currency symbol accrding to your contry.
    except AttributeError:
        products.append(product)
        stars.append(star)
        prices.append('Rs. '+price.lstrip('₹'))

#print(products,stars,prices)


# *****Save scrapped product info into .csv file with search query as file name***** #
with open(search+'data.csv','a',newline='') as csv_file:
    empty_file = os.stat(search+'data.csv',).st_size==0
    Table=['Product','Star','Price']
    w=csv.DictWriter(csv_file, fieldnames = Table)
    if empty_file:
        w.writeheader()
    for j in range(len(products)):
        w.writerow({'Product':products[j],'Star':stars[j],'Price':prices[j]})
