import math
class Paralelogram:
    def __init__(self, height , length):
        self.heigth = height
        self.length = length
    def area(self):
        self.area = self.heigth * self.length
        return math.fabs(self.area)
