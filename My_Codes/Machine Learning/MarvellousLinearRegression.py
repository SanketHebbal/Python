import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def MarvellousRegression():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print(mean_x , mean_y) # 3 3.6

    # y = mx + c
    #calculate m

    n = 0
    d = 0
    
    for i in range(len(X)):

        n += (X[i] - mean_x)*(Y[i] - mean_y)
        d += (X[i] - mean_x)**2

    print(n,d) # 4 10

    m = n/d  
    print(m) # 0.4

    #y = mx + c   =>  mean_y = 0.4*mean_x + c


    #calculate c

    c = mean_y - 0.4*mean_x
    print(c)

    #final equation is  y = 0.4x + 2.4
    #give value of x and get predicted value of y


    x = np.linspace(1,6,5)
    print(x)
    y = m*x + c
    print(y)

    plt.plot(x,y,color="#58b970",label="Regression Line")
    plt.scatter(X,Y , color="#ef5423" , label = "Scatter Points")

    plt.xlabel("X - Independent Variable")
    plt.ylabel("Y - Dependent Variable")

    plt.legend()
    plt.show()

    
def Main():

    MarvellousRegression()

if __name__ == "__main__":

    Main()
