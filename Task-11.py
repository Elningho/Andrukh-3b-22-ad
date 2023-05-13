class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def info(self):
        print('Имя собаки:', self.name, ', порода:', self.breed, ', возраст:', self.age)

dog1 = Dog('Тузик', 'Хаски', 3)
dog1.info()