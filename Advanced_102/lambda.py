# lambda, filter, reduce, map in python
# lambda functions are anonymous function because they dont have any name
# sometimes they are called one line function because they are written in a
# single line of code

# def double ( x ):
#     return x *2
# def add (x, y):
#     return x + y
# def product(x, y, z):
#     return x*y*z

# Lambda functions are generally used with the functions which takes function as an argument
# or retuens function as the result

from functools import reduce
double = lambda x: x * 2
add = lambda  x, y: x + y
product = lambda x, y, z: x*y*z

print(double(10))
print(add(10, 10))
print(product(10, 20, 50))
# Filter, Reduce and Map
my_list = [2, 5, 8, 9, 3, 4]
my_list2 = [3, 8, 7, 2, 1, 6]


a = map(lambda x: x * 2, my_list)
print(list(a))
b = map(lambda x, y: x + y, my_list, my_list2)
print(list(b))

c = filter(lambda x : x % 2 == 0, my_list)
print(list(c))
d = filter(lambda x : True if x > 5 else False, my_list)
print(list(d))
e = reduce(lambda x, y: x + y, my_list)
print(e)