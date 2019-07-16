class Arithematic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.result = 0
        
    def Accept(self):
        self.value1 = int(input("Enter first number ->"))
        self.value2 = int(input("Enter second number ->"))

    def Addition(self):
        self.result = self.value1 + self.value2
        return self.result
    
    def Multiplication(self):
        self.result = self.value1 * self.value2
        return self.result

    def Division(self):
        self.result = self.value1 / self.value2
        return self.result

    def Subtraction(self):
        self.result = self.value1 - self.value2
        return self.result

    def Display(self):
        print("Addition is {} Subtraction is {} Multiplication is {} Division is {}".format(obj1.Addition(),obj1.Subtraction(),obj1.Multiplication(),obj1.Division()))        

obj1 = Arithematic()
obj1.Accept()
obj1.Display()
