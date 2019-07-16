import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def MarvellousLinearRegression():
    
    reader = pd.read_csv("Advertising.csv")

    features = ['TV' , 'radio' , 'newspaper']

    data = reader[features].values
    target = reader['sales'].values

    # sales = C + m1(Tv) + m2(radio) + m3(newspaper)

    ones = [1]*len(data) # coefficient of C
    
    X = np.array(data)  #coefficient of Tv - radio - newspaper

    X = np.column_stack((X,ones)) # X is an array of coefficients of independent variables

    Y = target  #Y is an array of dependent variables


    # m = ((X'X)^-1)X'Y
    X_transpose = np.transpose(X)

    result = np.dot(X_transpose,X)

    result_inverse = np.linalg.inv(result)

    ans = np.dot(result_inverse , X_transpose)

    M = np.dot(ans,Y)  # M is an array of slopes

    y_predict = list()

    for i in range(len(data)):
        y_predict.append(M[0]*data[i][0] + M[1]*data[i][1] + M[2]*data[i][2] + M[3])

    print(y_predict)

    reg = LinearRegression()
    reg.fit(data,target)
    predict = reg.predict(data)

    print(predict)

def Main():

    MarvellousLinearRegression()


if __name__ == "__main__":
    Main()
