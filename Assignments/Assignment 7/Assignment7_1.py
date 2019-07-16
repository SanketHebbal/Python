class BookStore:
    no_of_books = 0

    def __init__(self, name , author):

        self.Name = name
        self.Author = author
        BookStore.no_of_books += 1

    def Display(self):
        print("{} by {}. No of books {}".format(self.Name,self.Author,BookStore.no_of_books))


def AcceptName():
    return input("Enter name of book ->")

def AcceptAuthor():
    return input("Enter author of book ->")
    
obj1 = BookStore(AcceptName(),AcceptAuthor())
obj1.Display()

obj2 = BookStore(AcceptName(),AcceptAuthor())
obj2.Display()

obj3 = BookStore(AcceptName(),AcceptAuthor())
obj3.Display()
