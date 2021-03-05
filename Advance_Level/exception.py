# # a = float(input("Enter Number 1: "))
# # b = float(input("Enter Number 2: "))
# # result = None
# # try:
# #     result = a / b
# # except ZeroDivisionError as e:
# #     print("float division by zero =",type(e))
# #
# # except ValueError as e:
# #     print("ValueError =", type(e))
# #
# # except TypeError as e:
# #     print("typeError = ", type(e))
# # # THe else will only be executed when your program throws an error
# # else:
# #     print("___else___")
# # #The keyword finally will always be executed whither there is an erroe or now
# # #which can be used to reinitiate the connection to a database should the connection get lost in the way
# # finally:
# #     print("finally")
# #
# # print("Result is = ",result)
# # print("End")
#
# #RAISING EXCEPTION
#
# class CoffeeCup:
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def drink_coffee(self):
#         if self.__temperature > 85:
#             # print("Coffee is too Hot")
#             raise Exception("Coffee too Hot")
#
#         elif self.__temperature < 65:
#             # print("Coffee is too Cold")
#                 raise ValueError('coffee to cold')
#
#         else:
#             print("Coffee is OKay")
#
#
# cup = CoffeeCup(10)
# cup.drink_coffee()


# CUSTOM EXCEPTION
class CoffeeTooHotException(Exception):
    def __init__(self, Msg):
        super().__init__(Msg)

class CoffeeTooColdException(Exception):
    def __init__(self, Msg):
        super().__init__(Msg)


class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            # print("Coffee is too Hot")
            raise CoffeeTooHotException("Coffee too Hot:" + str(self.__temperature))

        elif self.__temperature < 65:
            # print("Coffee is too Cold")
            raise CoffeeTooColdException('coffee to cold:' + str(self.__temperature))

        else:
            print("Coffee is OKay")


cup = CoffeeCup(100)
cup.drink_coffee()
