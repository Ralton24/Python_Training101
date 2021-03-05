class Poligon:
    __height = None
    __width = None

    def set_value(self, height, width):
        self.__height = height
        self.__width = width
    def get_height(self):
        return self.__height
    def get_with(self):
        return self.__width


# class Rectangle(Poligon):
#     def area(self):
#         return self.get_height() * self.get_with()
#
# class Triangle(Poligon):
#     def area(self):
#         return self.get_height() * self.get_with() /2
#
#
# rect = Rectangle()
# tri = Triangle()
#
# rect.set_value(50, 50)
# tri.set_value(50, 50)
# print(rect.area())
# print(tri.area())
#
