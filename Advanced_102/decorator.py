# A decorator wrap a function and modify its behavior  in one way or the other
# without having to directly chanage the source code of the function being decorated

# def decorator_func(func):
#     def wrapper_func():
#         print('x' * 20)
#         func()
#         print('y' * 20)
#
#     return wrapper_func
#
#
# @decorator_func
# def say_hello():
#     print("Hello World")

# hello = decorator_func(say_hello)
# hello()


# def decorator_divide(func):
#     def wrapper_func(a, b):
#         print('Divide', a, 'and', b)
#         if b == 0:
#             print("Division with Zero is not allowed")
#             return 0
#         return a / b
#
#     return wrapper_func
# @decorator_divide
# def divide(x, y):
#     return x / y
#
# print(divide(5, 10))

from time import time
def timing(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        print(start)
        result = func(*args, **kwargs)
        end = time()
        print(end)
        print('Elapsed time: {}'.format(end - start))
        return result

    return wrapper_func

@timing
def my_func(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum
print(my_func(20000000))



