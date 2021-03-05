#class Parent:
    #  HOW TO USE "SUPER"
#     def __init__(self, name):
#         print('__init__parent', name)
#
# class Child (Parent):
#     def __init__(self):
#         print('__child__parent',)
#         super().__init__('Max')
#
#
# child = Child()

class Parent:
        def __init__(self, name):
            print('__init__parent', name)

class Parent2(Parent):
        def __init__(self, name):
            print("parent2__init__", name)

class Child(Parent2, Parent):
        def __init__(self):
            print('__child__parent')
            Parent2.__init__(self,'max')
            Parent.__init__(self,'tom')
child = Child()
print(Child.__mro__)

