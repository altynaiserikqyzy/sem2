class Area:
    def __init__(self , h , a , b):
        self.a = a 
        self.b = b
        self.h = h
    def area(self):
        self.area = 0.5 * (self.a + self.b) * self.h
        return self.area
a = Area(5,4,6)
print(a.area())
