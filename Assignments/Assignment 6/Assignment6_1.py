class Demo:
    value = None;

    def __init__(self,no1,no2):
        self.i = no1
        self.j = no2

    def fun(self):
        print(self.i,self.j)

    def gun(self):
        print(self.i,self.j)


obj1 = Demo(10,20)
obj2 = Demo(20,30)


obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()
