class Rectangle:
    #ENCAPSULATION
#     def __init__(self, height, width):
#         self.__height = height
#         self.__width = width
#
#     def set_height(self, height):
#         self.__height = height
#
#     def get_height(self):
#         return self.__height
#
#     def set_height(self, width):
#         self.__width = width
#
#     def get_height(self):
#         return self.__width
#     def area (self):
#         return self.__height * self.__width
#
#
#
#
# rect1 = Rectangle(20, 50)
# rect2 = Rectangle(50, 70)
#
# # rect1.height = 10
# # rect1.width = 20
# #
# # rect2.height = 50
# # rect2.width = 20
#
# print(rect1.area())
# print(rect2.area())
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_method(self):
        print(self.a)
        print(self._b)
        print(self.__c)
        print('public')
        self.__private_method()

    def __private_method(self):
        print('private')

hello = Rectangle('name')
print(hello.a)
print(hello._b)

hello.public_method()

