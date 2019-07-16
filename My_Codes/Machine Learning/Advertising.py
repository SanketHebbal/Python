import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def MarvellousLinearRegression():
    
    reader = pd.read_csv("Advertising.csv")

    features = ['TV' , 'radio' , 'newspaper']

    data = reader[features].values
    target = reader['sales'].values

    train_data , test_data , train_target ,test_target = train_test_split(data , target , test_size = 0.5)
    
    # using inbulit algorithm
    '''
    reg = LinearRegression()
    reg.fit(train_data,train_target)
    predict = reg.predict(test_data)
    '''
    
    # using user defined algorithm

    ones = [1]*len(reader['TV'].values) # coefficient of C    
    X = np.array(reader['TV'].values)  #coefficient of Tv - radio - newspaper
    X = np.column_stack((X,ones)) # X is an array of coefficients of independent variables
    Y =   #Y is an array of dependent variables


    # m = ((X'X)^-1)X'Y
    X_transpose = np.transpose(X)

    result = np.dot(X_transpose,X)

    result_inverse = np.linalg.inv(result)

    ans = np.dot(result_inverse , X_transpose)

    M = np.dot(ans,Y)  # M is an array of slopes

    y_predict = list()

    
    for i in range(len(reader['TV'].values)):
        y_predict.append(M[0]*reader['TV'].values[i] + M[1])

    
    #   actual_value   predicted_by_inbuilt_algorithm    predicted_by_user_defined_algorithm
    
    '''
    for i in range(len(test_target)):
        print(str(test_target[i]) + "    " + str(predict[i]) + "    " + str(y_predict[i]))
    '''


        
    max_x = np.max(reader['TV'].values)
    min_x = np.min(reader['TV'].values) 

    x = np.linspace(min_x , max_x , len(reader['TV']))

    y = M[0]*x + M[1]

    plt.plot(x,y,color="#58b970",label="Regression Line")
    plt.scatter(reader['TV'].values , target , color = "#ef5423" , label = "Points")




    plt.show()
    
def Main():

    MarvellousLinearRegression()


if __name__ == "__main__":
    Main()
