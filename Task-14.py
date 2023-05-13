class Student:
    def __init__(self, name, surname, age, major):
        self.name = name
        self.surname = surname
        self.age = age
        self.major = major

    def info(self):
        print(f'{self.name} - {self.surname}, {self.age} лет, специальность - {self.major}')


student1 = Student('Иван', 'Иванов', 17, 'Програмист')
student1.info()