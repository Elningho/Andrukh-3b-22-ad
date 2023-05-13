class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def rectangle_area(self):
        print('Площадь прямоугольника:', self.length * self.width)


Rectangle1 = Rectangle(4, 5)
Rectangle1.rectangle_area()
