import pandas as pd
from sklearn import tree
from sklearn import preprocessing
from scipy.spatial import distance
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


'''
 overcaste 0
 rainy 1
 sunny 2
 
 cold 0
 hot 1
 mild 2
 
 no 0
 yes 1
 
'''

filename = r"C:\Users\Sanket\Downloads\Python\Notes\Mails\Machine Leaning\MarvellousInfosystems_PlayPredictor.xlsx"

def CheckAccuracy(data1 , data2):
    return accuracy_score(data1,data2)

def Main():

    reader = pd.read_excel(filename , skiprows = 1)
    le = preprocessing.LabelEncoder()
    
    for column in reader.columns:
        reader[column] = le.fit_transform(reader[column])

    label = ['Play']
    feature = ['Wether','Temperature']

    data = reader[feature]
    target = reader[label]
    
    train_data , test_data , train_target , test_target = train_test_split(data,target,test_size = 0.5)

    clf = KNeighborsClassifier(n_neighbors=7)
    clf.fit(train_data,train_target.values.ravel())
    prediction = clf.predict(test_data)

    print(CheckAccuracy(test_target , prediction ))
    
if __name__ == "__main__":
    Main()
