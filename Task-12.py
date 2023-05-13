class Student:
    def __init__(self, name, surname, year, subject1, subject2):
        self.name = name
        self.surname = surname
        self.year = year
        self.subject1 = subject1
        self.subject2 = subject2

    def average(self):
        print('Средний балл:', (self.subject1 + self.subject2) / 2)


Student1 = Student('Иван', 'Иванов', 1, 5, 4)
Student1.average()