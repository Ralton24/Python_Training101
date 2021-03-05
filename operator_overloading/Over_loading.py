import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius
        return radius

    def get_radius(self,):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2
    def __add__(self, circle_object):
        return Circle(self.__radius + circle_object.__radius)

    def __lt__(self, circle_object):
        return (self.__radius + circle_object.__radius)

    def __gt__(self, circle_object):
        return (self.__radius + circle_object.__radius)
n1 = Circle(2)
n2 = Circle(3)
C3 = n1 + n2

print(n1.get_radius())
print(n2.get_radius())
print(C3.get_radius())

print(n1 > n2)
print()
