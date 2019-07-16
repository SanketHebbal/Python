
def Myreverse(fun):

    def inner(string):
        print(fun.__name__)
        return "".join(fun(string))

    return inner

reversed = Myreverse(reversed)
print(reversed("Sanket"))

print(sum(i*i for i in range(10)))
