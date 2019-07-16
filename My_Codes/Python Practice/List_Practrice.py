import copy

componentList = []

while True:

    component = input("Enter a component name or Enter nothing to stop.")
    if component == "":
        break
    componentList += [component]
    
for name in componentList:
    print(name +"\t"+ str(componentList.index(name)))

arr = [['cat','dog'] , ['black','white']]
print(arr)

brr = copy.copy(arr)
print(brr)
