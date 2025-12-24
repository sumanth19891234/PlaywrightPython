class contrsuctorpractise:
    a =100

    def __init__(self,a,b):
        self.number1=a
        self.number2=b
        print("insode constructor")
    
    def getData(self):
        print("inside getdata method in a class")

    def __str__(self):
        return f"contrsuctorpractise(number1={self.number1}, number2={self.number2})"

    def summation(self):
        return self.number2+self.number1+contrsuctorpractise.a

    def summation2(self, c, d):
        return self.number2 + self.number1 + contrsuctorpractise.a+ c+d

construct=contrsuctorpractise(6,5)
print(construct)
print(construct.summation())
print(construct.summation2(10, 2))
print(construct.summation2(3, 4))
