from pygame import mixer
from Product import Product
import time

products = []  # product list
mixer.init()
mixer.music.load("found.mp3")

def loadProducts(fileName):
    inFile = open(fileName, "r")
    for line in inFile:
        l = line.split(",")
        products.append(Product(l[0], l[1], l[2]))
    #print(products)

def alarm():
    for x in range(5):
        mixer.music.play()
        time.sleep(2)

def stockHelper():
    stockFlag = False
    while True:
        for product in products:
            time.sleep(1)
            stockFlag = product.check()
            if stockFlag == True:
                return
        time.sleep(60)


def main():
    print("Starting")
    # mixer.music.play()
    loadProducts("urls.txt")
    stockHelper()
    print("Program exiting")


if __name__ == "__main__":
    main()
