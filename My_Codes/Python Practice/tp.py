def fun():
    print("Inside fun")

def gun(obj):

    print(obj.__name__)

gun(fun)
