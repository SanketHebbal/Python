import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



def MarvellousLinearRegression():
    
    reader = pd.read_csv("MarvellousHeadBrain.csv")

    features = ['Head Size(cm^3)']

    data = reader[features].values
    target = reader['Brain Weight(grams)'].values

    train_data , test_data , train_target , test_target = train_test_split(data,target,test_size = 0.5)
    
    reg = LinearRegression()
    reg.fit(train_data,train_target)
    predict = reg.predict(test_data)

    #print(test_data)
    #print(predict)

    # sales = C + m1(Tv) + m2(radio) + m3(newspaper)
    
    ones = [1]*len(train_data) # coefficient of C
    
    X = np.array(train_data)  #coefficient of Tv - radio - newspaper

    X = np.column_stack((X,ones)) # X is an array of coefficients of independent variables

    print(X)
    Y = test_target
    
    #= test_target.reshape((-1,1)) #Y is an array of dependent variables

    # m = ((X'X)^-1)X'Y
    X_transpose = np.transpose(X)

    result = np.dot(X_transpose,X)

    result_inverse = np.linalg.inv(result)

    ans = np.dot(result_inverse , X_transpose)

    M = np.dot(ans,Y)  # M is an array of slopes

    '''
    y_predict = list()

    for i in range(len(train_data)):
        y_predict.append(M[0]*test_data[i] + M[1])

    print(y_predict)
    '''
    X_mean = np.mean(train_data)
    Y_mean = np.mean(train_target)
    
    n = 0
    d = 0
    
    for i in range(len(train_data)):

        n += (train_data[i] - X_mean)*(train_target[i] - Y_mean)
        d += (train_data[i] - X_mean)**2

    m = n/d

    print(m)
    c = Y_mean - m*X_mean
    y = m*test_data[0] + c
    #print(y)
    
    print(M)
    
def Main():

    MarvellousLinearRegression()
    

if __name__ == "__main__":
    Main()
