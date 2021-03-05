# HOW TO USE MODULES IN A CLASS

from rectangle import Rectangle
from triangle import Triangle
rect = Rectangle()
tri = Triangle()

rect.set_color('red')
tri.set_color('blue')

rect.set_value(50, 50)
tri.set_value(50, 50)
print(rect.area())
print(tri.area())

print(rect.get_color())
print(tri.get_color())