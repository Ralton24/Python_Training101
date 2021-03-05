# THE __name__ =="__main__ is used to allow a specific code run
# even after importing it functions or class into
# another project or code

def add(a, b):
    return a + b
print(__name__)
if __name__ =="__main__":
    print(add(10, 7))