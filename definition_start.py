"""
- oop helps organize and structure code
- allows for grouping of data and behavior 
- promotes modularization of programs
- isolates different parts of the program so it's easier to identify where problems occur
- OOP Terms:
    - class: a blueprint for creating objects of a particular type
    - methods: regular functions that are part of a class
    - attributes: variables that hold data that are part of a class
    - object: a specific instance of a class
    - inheritance: Means by which a class can inherit capailites from another
    - composition: means of building complex objects out of other objects

"""

# create a basic class:

class Book:
    #the init function is called to initialize new object with information
    #self is automatically passed in
    #title is an attribute
    def __init__(self, title):
        self.title = title

# create an instance of the class:

b1 = Book("Brave New World")
b2 = Book("War and Peace")

# print class and property:

print(b1)
print(b1.title)
