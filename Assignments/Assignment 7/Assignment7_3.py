class Number:

    def __init__(self,number):
        self.Value = number

    def CheckPrime(self):

        if(self.Value < 2):
            return False
           
        for i in range(2,self.Value//2+1):
            if(self.Value % i == 0):
                return False
        return True
        
    def CheckPerfect(self):

        if(self.SumFactors() == self.Value):
            return True
        else:
            return False

    def Factors(self):
        
        print("Factors ",end=" ")
        for i in range(1,self.Value//2+1):
            if self.Value % i == 0 :
                print(i,end=" ")
        
    def SumFactors(self):
        
        sum = 0
        for i in range(1 , self.Value//2+1):
            if(self.Value % i == 0):
                sum += i
        return sum


num = int(input("Enter a number ->"))

obj1 = Number(num)
print("Prime ",obj1.CheckPrime())
print("Perfect ",obj1.CheckPerfect())
obj1.Factors()
print("\nSum of factors is {}".format(obj1.SumFactors()))
