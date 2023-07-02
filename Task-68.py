import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                  (title TEXT, genre TEXT, rating REAL)''')

movies = [('Фильм 1', 'Драма', 8.2), ('Фильм 2', 'Комедия', 7.6), ('Фильм 3', 'Боевик', 5.5), ('Фильм 4', 'Драма', 9.9)]
cursor.executemany('INSERT INTO movies VALUES (?, ?, ?)', movies)
conn.commit()

cursor.execute('SELECT * FROM movies WHERE genre = "Драма"')
selected_genre_movies = cursor.fetchall()
for movie in selected_genre_movies:
    print(f'Название: {movie[0]}, Жанр: {movie[1]}, Рейтинг: {movie[2]}')
conn.close()