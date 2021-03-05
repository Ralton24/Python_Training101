# HOW TO USE MODULES IN A CLASS

# from inheritance import Poligon
# class Triangle(Poligon):
#     def area(self):
#         return self.get_height() * self.get_with() /2




#MULTIPLE INHERITANCE
from inheritance import Poligon
from shape import Shape
class Triangle(Poligon, Shape):
    def area(self):
        return self.get_height() * self.get_with() /2