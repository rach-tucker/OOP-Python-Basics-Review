# create a basic class:

class Book:
    #the init function is called to initialize new object with information
    #self is automatically passed in
    #title is an attribute
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    #create instance method
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        #the ._ gives developers a hint that this attribute is internal to the class and should not be accessed outside the class's logic
        self._discount = amount

class Newspaper:
    def __init__(self, name):
        self.name = name

# create an instance of the class:

b2 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b1 = Book("The Catcher in the Rye", "JD Saliner", 234, 29.95 )
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# print class and property:

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

#use type function to find the type of ob object:

print(type(b1))
print(type(n1))

#compare two types (will return True or False:)
print(type(b1) == type(b2))
print(type(b1) == type(n2))


#use isinstance to check a specific instance (will return True or False:)
print(isinstance(b1, Book)) 
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))