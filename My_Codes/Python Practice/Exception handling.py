no1 = int(input("Enter first number ->"))
no2 = int(input("Enter second number ->"))


try:
    result = no1 / no2
    print(result)
except Exception:
    print("Unable to divide by zero")
finally:
    print("Inside finnaly")

