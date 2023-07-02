import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (name TEXT, age INTEGER, average_score REAL)''')

students = [('Имя 1', 29, 4.5), ('Имя 2', 19, 4.8), ('Имя 3', 21, 3.9), ('Имя 4', 20, 4.2)]
cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students)
conn.commit()

cursor.execute('SELECT * FROM students')
all_students = cursor.fetchall()
for student in all_students:
    print(f'Имя: {student[0]}, Возраст: {student[1]}, Средний балл: {student[2]}')
conn.close()