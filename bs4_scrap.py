from bs4 import BeautifulSoup as bs
import requests
#import json
import csv

stars=[]
titles=[]
prices=[]
avaibility=[]

url="http://books.toscrape.com/catalogue/page-1.html"

r=requests.get(url)
soup=bs(r.content, 'html5lib')
print('html page is scraped successfully.')
for t in soup.find_all('a', title = True):
    print(t)
    titles.append(t.attrs['title'])

for s in soup.findAll('p', class_='star-rating'):
    #print(s)
    for k,v in s.attrs.items():
        print('key :',k)
        print('value:',v)
        stars.append(v[1])

for p in soup.findAll('p', class_='price_color'):
    print(p)
    prices.append(p.get_text())

for i in soup.find_all('p', attrs = {'class': 'instock availability'}):
    instk=i.getText()
    avaibility.append(instk.strip())
#print(avaibility)
with open('web_scarp_data\\1_scrap.csv','w',newline='') as f:
    head=['Titles','Stats','Prices','Avability']
    w=csv.DictWriter(f,fieldnames = head)
    w.writeheader()
    for _ in range(len(titles)):
        w.writerow({'Titles':titles[_],'Stats':stars[_],'Prices':prices[_],'Avability':avaibility[_]})
print('html page writend to the file successfully.')
print("Is file closed :",f.closed)
#print(r.apparent_encoding)
#print(r.content)
#print(r.cookies)
#print(r.elapsed)
#print(r.encoding)
# print(r.headers)
#print(r.history)
#print(r.is_permanent_redirect)
#print(r.is_redirect)
#print(r.json())
#print(r.links)
#print(r.next)
#print(r.ok)
#print(r.reason)
#print(r.request)
#print(r.status_code)
#print(r.text)
#print(r.url)
