from CalculatorModule import *

no1 = int(input("Enter first number --> "))
no2 = int(input("Enter second number --> "))

res = Add(no1 , no2);
print("Addition is " , res)

res = Sub(no1 , no2);
print("Subtraction is " , res)

res = Mult(no1 , no2);
print("Multiplication is " , res)

res = Div(no1 , no2);
print("Division is " , res)
