class Schoolboy:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def study(self):
        print(f'Школьник {self.name} учится в {self.grade} классе.')

schoolboy1 = Schoolboy('Анатолий', 11)
schoolboy1.study()