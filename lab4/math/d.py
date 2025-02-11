class Paralelogram:
    def __init__(self, height , length):
        self.heigth = height
        self.length = length
    def area(self):
        self.area = self.heigth * self.length
        return self.area
a=Paralelogram(5,6)
print(a.area())