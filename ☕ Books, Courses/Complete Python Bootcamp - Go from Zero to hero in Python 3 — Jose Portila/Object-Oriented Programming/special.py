class Book:

    def __init__(self, title, author, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        x = f'Book name {self.title}\nAuthor is {self.author}\nPages are {self.pages}'
        return x

    def __len__(self):
        # return len(self.pages) [error]
        return len(str(self))
        # return str(self) [error]


book_1 = Book('Python Rocks', 'Jose', 250)
print(book_1)
print(len(book_1))
