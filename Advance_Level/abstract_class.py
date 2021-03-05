from abc import ABC, abstractmethod
class Sharp (ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def parameter(self): pass

class Square (Sharp):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side
    def parameter(self):
        return 4 * self.__side

square = Square(5)
print(square.area())
print(square.parameter())