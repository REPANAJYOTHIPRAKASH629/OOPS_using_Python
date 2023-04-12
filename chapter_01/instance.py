
# Todo: create a basic class
class Book:
    #the "init" function is called when the instance is created and ready to be initialized
    def __init__(self,title,author,pages,price):
        self.title = title
        #Todo: add properties
        self.author =author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret message"
        
    #Todo: create instance menthods 
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - self.price * self._discount
        else:
            return self.price
        
    def setdiscount(self,amount):
        self._discount = amount


#Todo: create some book instances
b1 = Book("swathi book","anyone",15,5)
b2 = Book("Sunday swathi book","sakshi",25,10)


#Todo: print the price of book1
print(b1.getprice())


#Todo: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# Todo: properties with double underscores are hidden by the interpreter
# print(b2.__secret) #error
print(b2._Book__secret)