'''
Product class for organizing information better :)
'''
import webbrowser as wb
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
from datetime import datetime
class Product:
    def __init__(self, productName, productWebsite, productURL):
        self.productName = productName
        self.productURL = productURL
        self.productWebsite = productWebsite
    def __str__(self):
        #"Vector3([{0},{1},{2}])".format(self.x, self.y, self.z)
        return  "Name: {0} Website: {1} URL: {2}".format(self.productName, self.productWebsite, self.productURL)

    def getProductName(self):
        return self.productName

    def getProductURL(self):
        return self.productURL

    def getProductWebsite(self):
        return self.productWebsite

    def setProductName(self, productName):
        self.productName = productName

    def setProductURL(self, productURL):
        self.productURL = productURL

    def setProductWebsite(self, productWebsite):
        self.productWebsite = productWebsite
        
    def check(self):
        #print(self)
        page = urlopen(self.productURL)
        #print("URL oppened")
        html = page.read().decode("utf-8")
        #print("HTML decoded")
        soup = BS(html, "html.parser")
        #print("SOUP BSed")
        pageString = cleanString(soup.text)
        
        print(datetime.now().strftime("%H:%M:%S"), self.productName, self.productWebsite, end=" ")
        if "outofstock" in pageString.lower() or "soldout" in pageString.lower():
            print("Out of stock. :(")
            return False
        wb.open(self.productURL, new=2)
        print("STOCK FOUND!")
        alarm()
        return True

def cleanString(string):
    newString = ""
    vetoList = " \t\n"
    for char in string:
        if char not in vetoList:
            newString = newString + char
    return newString
