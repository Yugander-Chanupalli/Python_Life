'''
single inheritance
multilevel inheritance
multiple inheritance
hierachical inheritance

'''

# Single Inheritance
class Parent():
    def output(self):
        print("parent")

class child(Parent):
    def outputc(self):
        print("child")
    
c=child()
c.outputc()
c.output()


# MultiLevel Inheritance
class GrandParent():
    def outputgf(self):
        print("i am grand")
class Parent(GrandParent):
    def outputp(self):
        print("i am parent")
class child(Parent):
    def outputc(self):
        print("i am child")

c=child()
c.outputc()
c.outputp()
c.outputgf()


# Multiple Inheritance
class father():
    def outputf(self):
        print("i am father")

class mother():
    def outputm(self):
        print("i am mother")

class child(father,mother):
    def outputc(self):
        print("i am child")

c=child()
c.outputc()
c.outputf()
c.outputm()


# Hierachical inheritance
class father():
    def outputf(self):
        print("i am father")
class child1(father):
    def outputc1(self):
        print("i am child1")
class child2(father):
    def outputc2(self):
        print("i am child2")

c1=child1()
c2=child2()
c1.outputc1()
c1.outputf()
c2.outputc2()
c2.outputf()