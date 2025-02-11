import math
class DegreetoRadian:
    def __init__(self , degree ):
        self.degree = degree
    def convert(self):
        self.radian = self.degree * math.pi / 180
        return math.fabs(self.radian)
