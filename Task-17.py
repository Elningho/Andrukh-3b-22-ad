class Book:
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre

    def info(self):
        print(f'{self.name}, {self.author} ({self.year}), {self.genre}')

book1 = Book('Война и Мир', 'Л.Н.Толстой', 1865, 'роман')
book1.info()