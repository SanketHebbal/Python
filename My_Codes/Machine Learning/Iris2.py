from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree


iris = load_iris()

print(iris.feature_names)

print(iris.target_names)

test_index = [1,51,101]

target_data = np.delete(iris.target,test_index)
train_data = np.delete(iris.data , test_index ,axis=0)

test_target = iris.target[test_index]
test_data = iris.data[test_index]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,target_data)
result = clf.predict([[3.4,4.3,2.2,3.8]])


#visualisation

from sklearn.externals.six import StringIO
import pydot


dot_data = StringIO()

tree.export_graphviz(clf,out_file=dot_data,feature_names=iris.feature_names,class_names = iris.target_names,filled=True,rounded=True,impurity=False)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("ir.pdf")
