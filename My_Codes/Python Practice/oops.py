class Demo:

    i = None
    j = None
    
    def __init__(self,no1,no2):
        self.i = no1
        self.j = no2

    def fun(self):
        print(self.i , self.j)

    
obj1 = Demo(10,20)
obj1.fun()
