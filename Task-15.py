class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def info(self):
        print(f'{self.brand} - {self.model}, год выпуска: {self.year}, цена: {self.price}')

car1 = Car('BMW', 'X6', 2020, 5000)
car1.info()
