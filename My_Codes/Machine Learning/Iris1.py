from sklearn.datasets import load_iris

iris = load_iris()

print(iris.feature_names)

print(iris.target_names)

for i in range(1 ,len(iris.data) , 50):
    print(iris.data[i] , iris.target[i])


