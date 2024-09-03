def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(*a): #arbitary arguments stored as tuple
    print(a)

def mul1(**a): #keyword arguments stored as dictonary
    print(a)

add(1,2)
sub(4,2)
mul(1,2,3,4)
mul1(a=1,b=2,c=3,d=4)
