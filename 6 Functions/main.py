def A():
    B()
    print("A")

def B():
    C()
    print("B")

def C():
    A()#
    print("C")

A()
# RecursionError: maximum recursion depth exceeded

# List compresion.
List = [x for x in range(5)]
print(List)

