# FILE HANDLING IN PYTHON

# fh = open('demo.txt', 'w')
#
# fh.write("This file has being writing successfully:")
# fh.close()


# fh = open('demo.txt', 'w')
# try:
#     for i in range(10):
#         # fh.write("This file has being writing successfully: %d\n " % i)
#         fh.write("This file has being writing successfully: %d\n" % (i + 1))
# finally:
#     fh.close()

# OR IT CAN BE WRITING LIKE THIS IN A SHORTER FORM
# with open('demo.txt', 'w') as fh:
#     for i in range(10):
#         # fh.write("This file has being writing successfully: %d\n " % i)
#         fh.write("This file has being writing successfully: %d\n" % (i + 1))

# with open('C:\\Users\Raelton\Documents\Duckto\hack\\demo.txt', 'w') as fh:
#     for i in range(10):
#         # fh.write("This file has being writing successfully: %d\n " % i)
#         fh.write("This file has being writing successfully: %d\n" % (i + 1))


#HOW TO READ FROM A FILE IN PYTHON

# fh = open('demo.txt', 'r') #specify the file path
# print(fh.read()) #but to read a specific line you can pass the number as an argument
# print(fh.readline()) #this is to read an entire line
# print(fh.readlines()) #this will print the file in form of a list
# print(fh.readlines(5))

# in other to print the line one after the other, you will have to use for loop
# for line in fh:
#     print(line)
#     print(len(line)) #this is to count the number of words in each line
#     print(line.split())
#     print(len(line.split()))

# fh.close()

with open('demo.txt', 'r') as fh:
    for line in fh:
        print(len(line.split()))
