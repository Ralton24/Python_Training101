# HOW TO USE MODULES IN A CLASS

# from inheritance import Poligon
# class Rectangle(Poligon):
#     def area(self):
#         return self.get_height() * self.get_with()




#MULTIPLE INHERITANCE
from inheritance import Poligon
from shape import Shape
class Rectangle(Poligon, Shape):
    def area(self):
        return self.get_height() * self.get_with()