import tensorflow as tf


#1

'''
node1 = tf.constant(3.0,tf.float32)
node2 = tf.constant(4.0,tf.float32)

sobj = tf.compat.v1.Session()
print(sobj.run([node1,node2]))
sobj.close()
'''

#2

'''
node1 = tf.constant(3,tf.float32)
node2 = tf.constant(4,tf.float32)

output = node1 * node2

sobj = tf.compat.v1.Session()
print(sobj.run(output))
'''

#3
'''
n = []
for i in range(5):
    num = int(input("Enter a number "))
    n.append(num)


node1 = tf.placeholder(tf.float32)
node2 = tf.placeholder(tf.float32)

output = node1 * node2

sobj = tf.compat.v1.Session()

file_write = tf.compat.v1.summary.FileWriter("Demo",sobj.graph)

print(sobj.run(output,{node1:n , node2:n}))
'''

#4

w = tf.compat.v1.Variable([ 0.3 ], tf.float32)
b = tf.compat.v1.Variable([ -0.3 ] , tf.float32)

x = tf.compat.v1.placeholder(tf.float32)

linear_model = w*x + b          # calculated

y = tf.compat.v1.placeholder(tf.float32)    # expected

squared = tf.square(linear_model - y)
loss = tf.reduce_sum(squared)

init = tf.compat.v1.global_variables_initializer()

optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss) 
    
sobj = tf.compat.v1.Session()
sobj.run(init)

for i in range(100):
    
    print(sobj.run(loss,{x:[1,2,3,4] , y:[0,-1,-2,-3]}))
    print(sobj.run(w))
    print(sobj.run(b))

    sobj.run(train,{x:[1,2,3,4] , y:[0,-1,-2,-3]})

