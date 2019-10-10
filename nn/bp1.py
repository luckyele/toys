# 定义神经网络的模型架构

import numpy as np


# 计算loss函数
# network_y 计算出来目标值，real_y为真实值
def loss_der(network_y, real_y):
    return (network_y - real_y)

# 激活函数 sigmoid()
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# 对激活函数求导
def sigmoid_der(z):
    return sigmoid(z) * (1 - sigmoid(z))

# 前向传播算法
def feedForward(intput_a, weight, bias):
    f = lambda x:1./1.+ np.exp(-x)
    output_a = f(np.dot(weight, intput_a) + bias)
    return output_a

# 后向传播(BP)算法实现
def backprog(x, y):
    
    delta_w = [np.zeros(w.shape) for w in weights]
    delta_b = [np.zeros(b.shape) for b in biases]

    activation = x
    activations = [x]
    zs = []

    for w, b in zip(weights, biases):
        z = np.dot(w, activation) + b
        activation = sigmoid(z)
        activations.append(activation)
        zs.append(z)

    #BP1
    delta_L = loss_der(activations[-1], y) * sigmoid_der(zs[-1])

    #BP3
    delta_b[-1] = delta_L

    #BP4
    delta_w[-1] = np.dot(delta_L, activations[-2].transpose())
    
    delta_l = delta_L

    for l in range(2, num_layers):
        #BP2
        z = zs[-l]
        sp = sigmoid_der(z)
        delta_l = np.dot(weights[-l + 1].transpose(), delta_l) * sp
        #BP3
        delta_b[-l] = delta_l
        #BP4
        delta_w[-l] = np.dot(delta_l, activations[-l - 1].transpose())
    
    return (delta_w, delta_b)

 
if __name__ == "__main__":
    data = np.loadtxt('mess.csv',delimiter=',')
    network_sizes = [51,75,4]
    
    sizes = network_sizes
    num_layers = len(sizes)
    biases = [np.random.randn(h, 1) for h in sizes[1:]]
    weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
    
    training_x = np.array(data[0:1,0:51]).reshape(51,1)
    training_y = np.array([0,1,2,3]).reshape(4,1)
    #print("training data x:{}, training y:{}\n".format(training_x, training_y))
    w, b = backprog(training_x, training_y)

