import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books
                  (title TEXT, author TEXT, year INTEGER)''')

books = [('Книга 1', 'Автор 1', 1995), ('Книга 2', 'Автор 2', 1990), ('Книга 3', 'Автор 3', 2007), ('Книга 4', 'Автор 4', 2021)]
cursor.executemany('INSERT INTO books VALUES (?, ?, ?)', books)
conn.commit()

cursor.execute('SELECT * FROM books WHERE year > 2000')
books_after_2000 = cursor.fetchall()
for book in books_after_2000:
    print(f'Название: {book[0]}, Автор: {book[1]}, Год издания: {book[2]}')
conn.close()