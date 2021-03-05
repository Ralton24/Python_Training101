# # A GENERATOR IS A FUNCTION THAT RETURNS
# # THE ITERATOR OBJECT ON WHICH WE CAN ITERATE UPON
#
# # WHEN YOU USE A GENERATOR IT RETURNS THE ITERATOR OBJECT
#
# def my_func():
#
#     n = 1
#     print('----------------------------------------', n)
#     yield n
#     n += 1
#     print('----------------------------------------', n)
#     n += 1
#     yield n
#     n +=1
#     print('----------------------------------------', n)
#     yield n
#
# x = my_func() # generators are more simplier to use
# print(next(x))
# print(next(x))
# print(next(x))


def IteratorList(list):
    for i in list:
        yield i
a = [1, 2, 3, 4, 5, 6, 7,]

mylist = IteratorList(a)
for x in mylist:
    print(x)

# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# generators are more easy to use
# it is more efficient