import math
def volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)
radius = int(input())
print(volume_of_sphere(radius))