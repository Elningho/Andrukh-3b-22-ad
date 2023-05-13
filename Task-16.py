class Cat:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def info(self):
        print(f'Кошка по имени {self.name}, {self.age} лет, цвет {self.colour}')

cat1 = Cat('Мурка', 6, 'Белый')
cat1.info()