class Circle:
    
    PI = 3.14

    def __init__(self):

        self.Radius = 0
        self.Circumference = 0
        self.Area = 0

    def Calculate_Area(self):
        self.Area = Circle.PI*self.Radius*self.Radius

    def Calculate_Circumference(self):
        self.Circumference = 2*Circle.PI*self.Radius;

    def Accept(self):
        self.Radius = int(input("Enter radius -> "))

    def Display(self):
        print("Circle of radius {} has area {} circumference {}".format(self.Radius,self.Area,self.Circumference))

        
obj = Circle()
obj.Accept()
obj.Calculate_Circumference()
obj.Calculate_Area()
obj.Display()

obj1 = Circle()
obj1.Accept()
obj1.Calculate_Circumference()
obj1.Calculate_Area()
obj1.Display()
