from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
from sklearn.datasets import load_iris



class MarvellousKNN():

    def fit(self , train_data , train_target):
        self.train_data = train_data
        self.train_target = train_target
        
    def predict(self , test_data):
        
        prediction = list()
        for row in test_data:
            result = self.closest(row)
            prediction.append(result)

        return prediction        

    def closest(self , row):

        best_distance = edu(row,self.train_data[0])
        best_index = 0

        for i in range(1 , len(self.train_data)):
            dist = edu(row,self.train_data[i])
            if(dist < best_distance):
                best_distance = dist
                best_index = i

        return self.train_target[best_index]



def edu(a,b):
    return distance.euclidean(a,b)

def Main():

    iris = load_iris()

    data = iris.data
    target = iris.target

    train_data , test_data , train_target , test_target = train_test_split(data,target,test_size = 0.5)

    clf = MarvellousKNN()

    clf.fit(train_data , train_target)
    prediction = clf.predict(test_data)
    result = accuracy_score(test_target , prediction)
    print(result)
    
if __name__ == "__main__":

    Main()
