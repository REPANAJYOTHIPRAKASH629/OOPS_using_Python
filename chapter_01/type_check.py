
# Todo: create a basic class
class Book:
    def __init__(self,title):
        self.title  = title

class Newspaper:
    def __init__(self,name):
        self.name = name

# Create some instances of the classes
b1 = Book("Paper boy")
b2 = Book("Surgical empowerment")

n1 = Newspaper("Andhra Jyothi")
n2 = Newspaper("Enadu")

#  Todo: use type() to inspect the object type
print(type(b1))       # <class '__main__.Book'>
print(type(n1))       # <class '__main__.Newspaper'>

# Todo: compare two types together
print(type(b1)==type(b2))       # True
print(type(b1)==type(n1))       # False
print(type(n1)==type(n2))       # True
print(type(b1)==type(n2))       # False

# Todo: use isinstance to compare a specific instance to a known type
print(isinstance(b1,Book))
print(isinstance(n1,Newspaper)) 
print(isinstance(n1,Book))
print(isinstance(b2,object))