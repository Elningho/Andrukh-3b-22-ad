class Figure:
    def __init__(self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

    def info(self):
        print(f'Площадь - {self.area}, периметр - {self.perimeter}')

figure1 = Figure(20, 18)
figure1.info()
