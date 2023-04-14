class Book:
    #Todo: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    #Todo: double-underscore properties are hidden from other classes
    __booklist = None

    #Todo : create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES
    
    #Todo : create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self,newtitle):
        self.title = newtitle

    def __init__(self,title,booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype.")
        else:
            self.booktype = booktype

#Todo : access the class attribute
print("Book Types : ",Book.getbooktypes())

#Todo : create some book instances
b1 = Book("Title 1 ","HARDCOVER")
b2 = Book("Title 2 ","PAPERBACK")
    
#Todo : ue the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)