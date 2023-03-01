#Book, Magazine and Newspaper all have a title and price. We can better this code by adding inheritance.

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

class Magazine:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self. publisher = publisher
        self.price = price
        self.period = period

class Newspaper:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.publisher = publisher
        self.price = price
        self.period = period
    
b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "monthly")

print(b1.author)
print(n1. publisher)
print(b1.price, m1.price, n1.price)