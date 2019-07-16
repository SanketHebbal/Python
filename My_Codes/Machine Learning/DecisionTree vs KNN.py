from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris


def MarvellousDecisionTree():

    iris = load_iris()

    data = iris.data
    target = iris.target

    train_data , test_data , train_target , test_target = train_test_split(data,target,test_size=0.5) #split the data into 50% - train data and test data

    clf = tree.DecisionTreeClassifier()
    clf.fit(train_data,train_target)
    predection = clf.predict(test_data)

    result = accuracy_score(test_target , predection)   # (correct_Predictions / Number_of_prediction)
    print(result)



def MarvellousKNN():

    iris = load_iris()

    data = iris.data
    target = iris.target

    train_data , test_data , train_target , test_target = train_test_split(data,target,test_size = 0.5)

    clf = KNeighborsClassifier()

    clf.fit(train_data,train_target)

    prediction = clf.predict(test_data)

    result = accuracy_score(test_target,prediction)
    print(result)

if __name__ == "__main__":
    MarvellousDecisionTree()
    MarvellousKNN()
