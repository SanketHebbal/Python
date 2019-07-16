import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle


def read_dataset():

    df = pd.read_csv("sonar.csv")

    X = df[df.columns[0:60]].values
    y = df[df.columns[60]]

    encoder = LabelEncoder()
    encoder.fit(y)
    y = encoder.transform(y)
    Y = one_hot_encode(y)

    #print(X.shape)
    #print(Y.shape)

    return X,Y

def one_hot_encode(labels):

    n_labels = len(labels)
    n_unique_labels = len(np.unique(labels))
    one_hot_encode= np.zeros((n_labels,n_unique_labels))

    #important code
    #first np.arange(n_labels) will return an list of numbers ranging from 0 to n_labels(207)
    #second labels is an list of 1's and 0's where 1 = mine and 0 = rock
    #then one_hot_encode[np.arange(n_labels),labels] = 1 will be evaluted as
    #one_hot_encode[0,1] = 1        [0,1]
    #one_hot_encode[1,1] = 1        [0,1]
    #one_hot_encode[2,1] = 1        [0,1]
    #upto
    #one_hot_encode[104,0] = 1      [1,0]
    #one_hot_encode[105,0] = 1      [1,0]
    #one_hot_encode[207,0] = 1      [1,0]
    
    one_hot_encode[np.arange(n_labels),labels] = 1 
    return one_hot_encode

def multilayer_perceptron(x,weights,biases):

    #mutiply and add
    # y = W*x + b
    print(x.shape)
    print(weights['h1'].shape)
    print(biases['b1'].shape)


    layer_1 = tf.add(tf.matmul(x,weights['h1']),biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    
    layer_2 = tf.add(tf.matmul(layer_1 , weights['h2']) , biases['b2'])
    layer_2 = tf.nn.sigmoid(layer_2)

    layer_3 = tf.add(tf.matmul(layer_2 , weights['h3']) , biases['b3'])
    layer_3 = tf.nn.sigmoid(layer_3)
     
    layer_4 = tf.add(tf.matmul(layer_3 , weights['h4']) , biases['b3'])
    layer_4 = tf.nn.sigmoid(layer_4)
    
    outlayer = tf.matmul(layer_4 , weights['out']) + biases['out']
    return outlayer


def Main():
    X , Y = read_dataset()

    X , Y = shuffle(X,Y,random_state = 1)

    train_x  , test_x , train_y , test_y = train_test_split(X,Y,test_size=0.3 , random_state=415)

    learning_rate = 0.3
    training_epochs = 600

    cost_history = np.empty(shape = [1] , dtype = float)

    n_dim = X.shape[1]      # no of features
    n_class = 2         # no. of classes == Rock and mine

    model_path = "Marvellous"

    # define no of hidden layers and no of neurons in each hidden layer
    n_hidden_1 = 60
    n_hidden_2 = 60
    n_hidden_3 = 60
    n_hidden_4 = 60
    
    x = tf.compat.v1.placeholder(tf.float32,[None,n_dim])       #for taking input
    y_ = tf.compat.v1.placeholder(tf.float32,[None,n_class])        #for holding output

    W = tf.compat.v1.Variable(tf.zeros([n_dim,n_class]))        # 60 X 2
    b = tf.compat.v1.Variable(tf.zeros([n_class]))                      # 2 X 1 

    weights = {
                'h1' :  tf.Variable(tf.random.truncated_normal([n_dim , n_hidden_1])),                   # 60 X 60
                'h2' :  tf.Variable(tf.random.truncated_normal([n_hidden_1 , n_hidden_2])),         # 60 X 60
                'h3' :  tf.Variable(tf.random.truncated_normal([n_hidden_2 , n_hidden_3])),         # 60 X 60
                'h4' :  tf.Variable(tf.random.truncated_normal([n_hidden_3 , n_hidden_4])),         # 60 X 60
                'out' : tf.Variable(tf.random.truncated_normal([n_hidden_4 , n_class]))                 # 60 X 2
              }   

    biases = {
                'b1' :  tf.Variable(tf.random.truncated_normal([n_hidden_1])),
                'b2' :  tf.Variable(tf.random.truncated_normal([n_hidden_2])),
                'b3' :  tf.Variable(tf.random.truncated_normal([n_hidden_3])),
                'b4' :  tf.Variable(tf.random.truncated_normal([n_hidden_4])),
                'out' : tf.Variable(tf.random.truncated_normal([n_class]))
              } 


    init = tf.compat.v1.global_variables_initializer()

    saver = tf.compat.v1.train.Saver()

    y = multilayer_perceptron(x,weights,biases)

    cost_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = y , labels = y_))

    training_step = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)

    sess = tf.compat.v1.Session()
    sess.run(init)

    mse_history = []
    accuracy_history = []

    for i in range(training_epochs):
    
        print(i)    
        sess.run(training_step , feed_dict = {x:train_x , y_:train_y})
        cost = sess.run(cost_function , feed_dict = {x:train_x , y_:train_y})
        cost_history = np.append(cost_history,cost)
        correct_prediction = tf.equal(tf.argmax(y,1) , tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction , tf.float32))
        pred_y = sess.run(y,feed_dict = {x:test_x})
        mse = tf.reduce_mean(tf.square(pred_y - test_y))
        mse_ = sess.run(mse)
        accuracy = sess.run(accuracy,feed_dict = {x:train_x , y_:train_y})
        accuracy_history.append(accuracy)

    save_path = saver.save(sess,model_path)
    print("Model saved in file")

    plt.plot(accuracy_history)
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.show()

    plt.plot(range(len(cost_history)),cost_history)
    plt.axis([0,training_epochs,0,np.max(cost_history)/100])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show()

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.square(pred_y - test_y))
    print("Test Accuracy: ", (sess.run(y, feed_dict={x:test_x, y_:test_y} )))

# Print the final mean square error
    pred_y = sess.run(y, feed_dict={x:test_x})
    mse = tf.reduce_mean(tf.square(pred_y- test_y))
    print("MSE: %.4f" % sess.run(mse))

    File_writer = tf.compat.v1.summary.FileWriter("Naval",sess.graph)

    
if __name__ == "__main__":
    Main()
