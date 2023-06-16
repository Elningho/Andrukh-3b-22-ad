class ProductCard:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = max(cost, 0)
        self.quantity = quantity

    def decrease_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1

    def change_cost(self, new_cost):
        if new_cost >= 0:
            self.cost = new_cost
        else:
            print('Ошибка: стоимость товара не может быть отрицательной!')


product = ProductCard('Молоток', 150, 10)
print(product.name)
print(product.cost)
print(product.quantity)

product.decrease_quantity()
print(product.quantity)

product.change_cost(149)
print(product.cost)

product.change_cost(-5)
