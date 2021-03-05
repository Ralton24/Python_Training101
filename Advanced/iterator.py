# # iteration is the act of going over a collection
# # e.g turples, set, lsit, dictionaries
# # or iterator is an objectet that can used to iterate over a collection
# # iterator has two methods which are __iter__() and __nect__()
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# it = iter(a)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# it = iter(a)
# a
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# next(a)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: 'list' object is not an iterator
# next(it)
# 1
# next(it)
# 2
# next(it)
# 3
# next(it)
# 4
# next(it)
# 5
# next(it)
# 6
# next(it)
# 7
# next(it)
# 8
# next(it)
# 9
# next(it)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration

# HOW TO CREATE A CUSTOM ITERATOR CLASS
class ListIterator:
    def __init__(self, list):
        self.__list = list
        self.__index = -1

    def __iter__(self):
        return self


    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__list):
            raise StopIteration
        return self.__list[self.__index]

    # def __next__(self):
    #     self.__index += 1
    #     return self.__list[self.__index]

a = [1, 2, 3, 4, 5, 6, 7,]
mylist = ListIterator(a)
it = iter(mylist)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for i in it:
    print(i)