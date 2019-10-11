# 定义神经网络的模型架构

import numpy as np
import random
import csv
import matplotlib.pyplot as plt

def nn_init():
    data = np.loadtxt('mess.csv', delimiter=',')
    network_sizes = [51, 4, 4]
    sizes = network_sizes
    num_layers = len(sizes)

    biases = [np.random.randn(h, 1) for h in sizes[1:]]
    weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
    #print(biases, weights)
    return data, network_sizes, num_layers, biases, weights

# 计算loss函数
def loss_der(network_y, real_y):
    return (network_y - real_y)

def calculate_loss(model, X, y):
    reg_lambda = 0.01
    num_example = len(X)
    probs = forward_proga(model, X)
    print(probs)

    #### something eror.
    corect_logprobs = -np.log(probs[range(num_example)])
    data_loss = np.sum(corect_logprobs)

    data_loss += reg_lambda / 2 * (np.sum(np.square(model['w1'])) + np.sum(np.square(model['w2'])))
    return 1. / num_example * data_loss

def forward_proga(model, x):
    w1, b1, w2, b2 = model['w1'],model['b1'],model['w2'],model['b2']
    z1 = w1.dot(x) + b1
    a1 = np.tanh(z1)
    z2 = w2.dot(a1) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return probs

# 激活函数 sigmoid()
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))
    #return np.exp(z)/np.sum(np.exp(z))

# 对激活函数求导
def sigmoid_der(z):
    return sigmoid(z) * (1 - sigmoid(z))

def predict(model, X):
    return np.argmax(forward_proga(model, X)) 

# 后向传播(BP)算法实现
def backprog(x, y, weights, biases, num_layers):
    
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

def save_model(model, t, r):
    '''保存模型（参数）、测试准确率'''
    with open('result%d.csv'%t,'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(model['w1'])
        f_csv.writerow(model['b1'])
        f_csv.writerow(model['w2'])
        f_csv.writerow(model['b2'])
        f_csv.writerow("%.2f"%r)

def training():    
    # 训练初始化
    data, network_sizes, num_layers, biases, weights = nn_init()
    model = {}
    losses = []
    model['w1'] = weights[0]
    model['w2'] = weights[1]
    model['b1'] = biases[0]
    model['b2'] = biases[1]

    training_times = int(data.shape[0] * 0.8)
    test_times = data.shape[0] - training_times

    # 训练模型 学习率 0.01
    for j in range(70):
        i = random.randint(0, training_times)
        training_x = np.array(data[i][0:51]).reshape(51,1)
        training_y = np.array([0,1,2,3]).reshape(4,1)
        a = int(data[:,51][i])
        l =  calculate_loss(model, training_x, a)
        losses.append(l)      
        weights, biases = backprog(training_x, training_y, weights, biases, num_layers)
        
        model['w1'] += weights[0]*(-0.01)
        model['w2'] += weights[1]*(-0.01)
        model['b1'] += biases[0]*(-0.01)
        model['b2'] += biases[1]*(-0.01)        

    # 测试模型并计算正确率
    j = 0 
    for i in range(test_times):
        k = random.randint(101,122)
        test_x = np.array(data[k][0:51]).reshape(51,1)
        a = int(data[:,51][k])
        b = int(predict(model, test_x))
        #print(a,b)

        if a == b:
            j = j + 1

    rate = j / test_times * 100
    print("right rate:%.2f%%\n"%rate)
   
    
    #保存模型及测试正确率
    save_model(model, rate, rate)

if __name__ == "__main__":
    
    for i in range(10000):
        training()
  

  