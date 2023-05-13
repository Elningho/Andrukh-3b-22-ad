class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


person1 = Person('Толя', 99)
person1.info()
