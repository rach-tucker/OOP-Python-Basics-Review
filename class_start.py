# create a basic class:

class Book:
    # properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    #double_underscore properties are hidden from other classes
    __booklist = None

    #create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    #create a static method(makes a class callable and not have its state modified)
    @staticmethod
    def getbooklist():
        if Book._booklist == None:
            Book._booklist = []
        return Book.__booklist

    def setTitle(self, newtitle):
        self.title - newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")

#acceses the class attribute
print("Book types: ", Book.getbooktypes())

b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")




print(b1)
print(b1.title)

#use the sdtatic method to access and singleton object

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
