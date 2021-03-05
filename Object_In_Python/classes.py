class Car:
#     def __init__(self, speed, color):
#         self.color = color
#         self.speed = speed
#
#     def set_speed(self, value):
#         self.speed = value
#
#     def get_speed(self):
#         return self.speed
#
#     def set_color(self, value):
#         self.color = value
#
#     def get_color(self):
#         return self.color
#
#
#
#
# ford = Car(200, 'red')
# honda = Car(20, 'blue')
# audi = Car(50, 'black')
# # ford.speed = 220
# # honda.speed = 200
# # audi.speed = 190
# #
# # ford.color = 'green'
# # honda.color = 'blue'
# # audi.color = 'red'
#
# print(ford.get_speed())
# print(ford.get_color())



                                        #ENCAPSULATION
    def __init__(self, speed, color):
        self.__color = color
        self.__speed = speed


    def set_speed(self, value):
        self.__speed = value


    def get_speed(self):
        return self.__speed


    def set_color(self, value):
        self.__color = value


    def get_color(self):
        return self.__color

ford = Car(200, 'red')
honda = Car(20, 'blue')
audi = Car(50, 'black')

print(ford.get_speed())
print(ford.get_color())