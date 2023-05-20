class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def info(self):
        print(f'Имя: {self.name}, Возраст: {self.age}, Зарплата: {self.salary}')

employee1  = Employee('Иван', 20, 100500)
employee1.info()