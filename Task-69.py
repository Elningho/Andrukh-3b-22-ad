import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (name TEXT, position TEXT, salary REAL)''')

employees = [('Сотрудник 1', 'Менеджер', 50000), ('Сотрудник 2', 'Инженер', 48000), ('Сотрудник 3', 'Менеджер', 60000), ('Сотрудник 4', 'Аналитик данных', 300000)]
cursor.executemany('INSERT INTO employees VALUES (?, ?, ?)', employees)
conn.commit()

cursor.execute('SELECT name FROM employees WHERE position = "Менеджер"')
managers = cursor.fetchall()
for manager in managers:
    print(f'Имя: {manager[0]}')
conn.close()