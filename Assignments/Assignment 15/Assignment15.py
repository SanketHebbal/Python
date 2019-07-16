import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


filename = r"C:\Users\Sanket\Downloads\Python\Notes\Mails\Machine Leaning\WinePredictor.xlsx"

def Main():

    reader = pd.read_excel(filename , skiprows=1)
    
    label = ['Class']
    feature = [col for col in reader.columns if col not in label]
    
    target = reader[label]
    data = reader[feature]

    train_data , test_data , train_target , test_target = train_test_split(data,target,test_size = 0.6)

    clf = KNeighborsClassifier(n_neighbors = 3)
    clf.fit(train_data , train_target.values.ravel())
    prediction = clf.predict(test_data)
    print(accuracy_score(test_target , prediction)*100)

if __name__ == "__main__":

    Main()
