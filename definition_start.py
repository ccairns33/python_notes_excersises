# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self,title):
        self.title = title


# TODO: create instances of the class
b1 = Book("War and Peace")
b2 = Book("The Idiot")
# TODO: print the class and property
print(b1)
print(b1.title)