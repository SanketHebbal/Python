class Sparrow:
    def fly(self):
        print("Sparrow can fly")

    def walk(self):
        print("it walks")

class Airplane:
    def fly(self):
        print("Airplane can fly")

    def walk():
        print("it walks")
        
class Whale:
    def swim(self):
        print("Whale can swim")


def fun(entity):
    entity.fly()
    entity.walk()

    
fun(Sparrow())
fun(Airplane())
fun(Whale())
