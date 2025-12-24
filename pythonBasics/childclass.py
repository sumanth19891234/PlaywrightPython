
from pythonBasics.contrsuctorexample import contrsuctorpractise


class childc(contrsuctorpractise):
    num2 = 300

    def __init__(self, a, b):
        contrsuctorpractise.__init__(self,a, b)
        print("child class constructor")

    def summchild(self):
        return  self.number1+self.number2 + childc.num2

    def summchild2(self):
        return  self.summation()+self.summation2(5,6)



child = childc(7,9)

print(child.summchild())
print(child.summchild2())

