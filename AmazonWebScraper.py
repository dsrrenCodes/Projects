from bs4 import BeautifulSoup
import requests


url="https://www.amazon.com/s?k=playstation+5&crid=2U1A61UK7E9W2&sprefix=playstatio%2Caps%2C642&ref=nb_sb_ss_ts-doa-p_1_10"

#headers to ensure web is recieved by genuine user
HEADERS=({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0","Accept-Language":"en-US, en;q=0.5"})

#http request 
req = requests.get(url,headers=HEADERS) 

#converting req to html format
doc=BeautifulSoup(req.content,"html.parser")

#obtained links and storing it in a list
links=doc.find_all("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
link=links[0].get("href")

#product link
productlist="https://amazon.com"+link

#repeat
newreq= requests.get(productlist,headers=HEADERS)

newdoc=BeautifulSoup(newreq.content,"html.parser")

productname=newdoc.find("span",{"id":"productTitle"},class_="a-size-large product-title-word-break").string.strip()
productprice=newdoc.find("span",class_="a-offscreen").string
productrating=newdoc.find("span",class_="a-icon-alt").string
productstock=newdoc.find("span",class_="a-size-medium a-color-success").string
print(productstock)

