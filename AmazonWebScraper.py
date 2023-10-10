from bs4 import BeautifulSoup
import requests

def main():
    
    
        #Amazon url playstation 5
        url="https://www.amazon.com/s?k=playstation+5&crid=2U1A61UK7E9W2&sprefix=playstatio%2Caps%2C642&ref=nb_sb_ss_ts-doa-p_1_10"

        #headers to ensure web is recieved by genuine user, #insert ur own user agent
        HEADERS=({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0","Accept-Language":"en-US, en;q=0.5"})

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
            #hmap["Stock"].append()
        return hmap




def get_title(doc):
    try:
        title=doc.find("span",{"id":"productTitle"},class_="a-size-large product-title-word-break").string.strip()
        
    
    #in the case where title cannot be found then return blank
    except(AttributeError):
        title= ""
    return title
    
    
def get_prices(doc):
    try:
        price=doc.find("span",class_="a-offscreen").string.strip()
        
        
    
    except(AttributeError):
        price= ""
    return price
    
def get_rating(doc):
    try:
        rating=doc.find("span",class_="a-icon-alt").string.strip()

    except(AttributeError):
        rating=""
        
    return rating

def get_stock(doc):
    try:
        stock=doc.find("span",class_="a-size-medium a-color-success").string.strip()
        
    except(AttributeError):
        stock="Not Stock"
    
    return stock
    

            
print(main())
