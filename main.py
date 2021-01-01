from urllib.request import urlopen
from pygame import mixer
from datetime import datetime
import time
import webbrowser as wb
from bs4 import BeautifulSoup as BS
from Product import Product
products = []  # product list
mixer.init()
mixer.music.load("found.mp3")

def loadProducts(fileName):
    inFile = open("urls.txt", "r")
    for line in inFile:
        l = line.split(",")
        products.append(Product(l[0], l[1], l[3]))


def cleanString(string):
    newString = ""
    vetoList = " \t\n"
    for char in string:
        if char not in vetoList:
            newString = newString + char
    return newString


def getStockNewegg(URL):
    page = urlopen(URL)
    html = page.read().decode("utf-8")
    soup = BS(html, "html.parser")
    productInventory = soup.find(
        "div", {"class": "product-inventory"}).get_text()
    if productInventory in " OUT OF STOCK.":
        return False
    return True


def getStockMemoryExpress(URL):
    page = urlopen(URL)
    html = page.read().decode("utf-8")
    soup = BS(html, "html.parser")
    productInventory = soup.find(
        "div", {"class": "c-capr-inventory__availability"}).get_text()
    productInventory = cleanString(productInventory)
    if "OutofStock" in productInventory:
        return False
    return True


def alarm():
    for x in range(5):
        mixer.music.play()
        time.sleep(2)


def stockChecker(choice):
    if choice in "newEgg":
        print(datetime.now().strftime("%H:%M:%S") +
              " Checking NewEgg stocking info...", end="")
        if getStockNewegg(URL):
            wb.open(URL, new=2)
            alarm()
            return True
        else:
            print("Stock not found :(")

    elif choice in "memoryExpress":
        print(datetime.now().strftime("%H:%M:%S") +
              " Checking MemoryExpress stocking info...", end="")
        if getStockNewegg(URL):
            wb.open(memExpressURL, new=2)
            alarm()
            return True
        else:
            print("Stock not found :(")
    else:
        print("Choice not found.")
    return False


def stockHelper():
    stockFlag = False
    while True:
        time.sleep(60)
        for product in products:
            time.sleep(1)
            stockFlag = product.check()


        stockFlag = stockChecker("newEgg")
        time.sleep(1)
        stockFlag = stockChecker("memoryExpress")
        if stockFlag == True:
            return


def main():
    print("Starting")
    # mixer.music.play()
    stockHelper()
    print("Stock found!\nprogram exiting")


if __name__ == "__main__":
    main()
