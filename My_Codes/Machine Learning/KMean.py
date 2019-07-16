import pandas as pd
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt

def MarvellousMean():

    center1 = np.array([1,1])
    center2 = np.array([5,5])
    center3 = np.array([8,1])

    data1 = np.random.randn(7,2) + center1
    data2 = np.random.randn(7,2) + center2
    data3 = np.random.randn(7,2) + center3

    data = np.concatenate((data1,data2,data3) , axis = 0)

    k = 3
    n = data.shape[0]
    c = data.shape[1]

    mean = np.mean(data,axis=0)
    std = np.std(data)
    centers = np.random.randn(k,c)*std + mean

    plt.scatter(data[:,0] , data[:,1] ,s=8 , c='r') #s is size of points
    plt.scatter(centers[:,0] , centers[:,1],marker="*", c='g' , s=100)

    center_old = np.zeros(centers.shape)
    center_new = deepcopy(centers)

    data.shape
    clusters = np.zeros(n)
    distances = np.zeros((n,k))

    print(center_new-center_old)
    
    error = np.linalg.norm(center_new - center_old)
    print(error)
def Main():

    MarvellousMean()
        
if __name__ == "__main__":
    Main()
