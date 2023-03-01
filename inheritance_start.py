#Book, Magazine and Newspaper all have a title and price. We can better this code by adding inheritance.
#below is a "class hierarchy"


#create a class with title and price so other classes can inherit from it
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

#create a class that inherits from Publication but has other attributes for Magazine and Newspaper
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)
    
b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "monthly")

print(b1.author)
print(n1. publisher)
print(b1.price, m1.price, n1.price)