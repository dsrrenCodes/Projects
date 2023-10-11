from bs4 import BeautifulSoup
from tabulate import tabulate
import requests
#Using bs4 to obtain data from a given url and storing data in a dictionary. 
#Using tabulate module to convert data in the dictionary into a table as output
#get_title gets name of product
#get_prices gets the price of the product
#get_rating gets the rating of the product
#get_stock gets the availability of the product
def main():
    
    
        #Insert own amazon link
        url=""

        #headers to ensure web is recieved by genuine user, #insert ur own user agent
        HEADERS=({"User-Agent":" ","Accept-Language":"en-US, en;q=0.5"})

        #http request 
        req = requests.get(url,headers=HEADERS) 

        #converting req to html format  
        doc=BeautifulSoup(req.content,"html.parser")

        #obtained links and storing it in a list, #listform
        links=doc.find_all("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")

        linklists=[]
        
        hmap={"Title":[], "Prices":[], "Rating":[], "Stock":[]}
        
        #taking lists and storing into linklists variable
        for link in links:
            L=link.get("href")
            linklists.append(L)
            
            
        for link in linklists:
            newurl="https://www.amazon.com"+link
            newreq=requests.get(newurl,headers=HEADERS)
            newdoc=BeautifulSoup(newreq.content,"html.parser")
            hmap["Title"].append(get_title(newdoc))
            hmap["Prices"].append(get_prices(newdoc))
            hmap["Rating"].append(get_rating(newdoc))
            hmap["Stock"].append(get_stock(newdoc))
        
        print(tabulate(hmap,headers=["Title","Prices","Rating","Stock"],tablefmt="presto"))
            
        




def get_title(doc):
    try:
        title=doc.find("span",{"id":"productTitle"},class_="a-size-large product-title-word-break").string.strip()
        
    #in the case where title cannot be found then return blank
    except(AttributeError):
        title=""
    
    return title
    
    
def get_prices(doc):
    try:
        price=doc.find("span",class_="a-offscreen").string.strip()

    #in the case where price cannot be found then return blank
    except(AttributeError):
        price=""
    return price

    
def get_rating(doc):
    try:
        rating=doc.find("span",class_="a-icon-alt").string.strip()

    #in the case where rating cannot be found then return blank
    except(AttributeError):
        rating=""
    
    return rating

def get_stock(doc):
    try:    
        stock=doc.find("span",class_="a-size-medium a-color-success").string.strip()

    #in the case where availability of stock cannot be found then return blank
    except(AttributeError):
        stock="No Stock"
    
    return stock

    
if __name__=="__main__":
    main()
