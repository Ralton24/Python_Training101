# nexted funtion is the act of definiing a function inside another function
def outFunc(Text):
    def innerFunc():
        print(Text)

    return innerFunc()

outFunc("Hello")
