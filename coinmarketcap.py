from bs4 import BeautifulSoup
import requests

url="https://coinmarketcap.com/"

req=requests.get("https://coinmarketcap.com/")

doc=BeautifulSoup(req.content,"html.parser")

a=doc.tbody

b=a.contents

prices={}
for i in b[0:10]:
    name,price= i.contents[2:4]

    Cryptoname=name.p.string
    Cryptoprice=price.a.string
    
    prices[Cryptoname]=Cryptoprice
print(prices)
