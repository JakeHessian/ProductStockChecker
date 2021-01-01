'''
Product class for organizing information better :)
'''

class Product:
    def __init__(self, productName, productWebsite, productURL):
        self.productName = productName
        self.productURL = productURL
        self.productWebsite = productWebsite

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
        if productWebsite.lower() in "newegg":
            getStockNewegg(productURL)
        elif productWebsite.lower() in "memoryexpress":
            getStockMemoryExpress(productURL)
        else:
            print("Error: website name not found.")
            return