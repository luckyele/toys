# 定义神经网络的模型架构

import numpy as np
import random
import csv
import time
import matplotlib.pyplot as plt

def nn_init():
    data = np.loadtxt('mess.csv', delimiter=',')
    network_sizes = [data.shape[1]-1,2,4]
    sizes = network_sizes
    num_layers = len(sizes)
    
    biases = [np.random.randn(h, 1) for h in sizes[1:]]
    weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
    #print(biases, weights)
    return data, network_sizes, num_layers, biases, weights

def to_one(data):

    data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    return data

# 计算loss函数
def loss_der(network_y, real_y):
    return (network_y - real_y)

def calculate_loss(model, X, y):
    reg_lambda = 0.001
    num_example = len(X)
    probs = forward_proga(model, X)
    #print(probs)

    #### something eror.
    corect_logprobs = -np.log(probs -y  + 1e-10)

    data_loss = np.sum(corect_logprobs)

    # 正则化
    data_loss += reg_lambda / 2 * (np.sum(np.square(model['w1'])) + np.sum(np.square(model['w2'])))
    return 1. / num_example * data_loss

def forward_proga(model, x):
    w1, b1, w2, b2 = model['w1'], model['b1'], model['w2'], model['b2']
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

def save_model(model):
    '''保存模型（参数）'''
    with open('result%d.csv'%time.time(),'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(model['w1'])
        f_csv.writerow(model['b1'])
        f_csv.writerow(model['w2'])
        f_csv.writerow(model['b2'])

def split_dataset(data):
    train_num = int(data.shape[0] * 0.7)
    s1 = slice(0,train_num)
    s2 = slice(train_num, data.shape[0])
    train_data = data[s1] 
    test_data = data[s2]
    return train_data, test_data

def training():    
    # 训练初始化
    learing_rate = 0.0001
    data, network_sizes, num_layers, biases, weights = nn_init()
    train_data, test_data = split_dataset(data)
    n_rows, n_cols =  train_data.shape
    
    model = {}
    losses = []
    model['w1'] = weights[0]
    model['w2'] = weights[1]
    model['b1'] = biases[0]
    model['b2'] = biases[1]

    # 训练模型 学习率 0.01
    for j in range(200):
        training_x = np.array(train_data[j % n_rows][0:n_cols-1]).reshape(n_cols-1,1)
        training_y = np.array([0,1,2,3]).reshape(4,1)
        a = int(train_data[:,n_cols-1][j % n_rows])
        l =  calculate_loss(model, training_x, a)
        print("iteration %d: loss %f" %(j, l))
        losses.append(l) 
        
        weights, biases = backprog(training_x, training_y, weights, biases, num_layers)
        
        model['w1'] += weights[0]*(-learing_rate)
        model['w2'] += weights[1]*(-learing_rate)
        model['b1'] += biases[0]*(-learing_rate)
        model['b2'] += biases[1]*(-learing_rate)        


        #保存模型及测试正确率
#    save_model(model)
    return losses

def test_preditc(model, test_data):
    '''测试模型并计算正确率'''
    j = 0
    n_rows, n_cols =  test_data.shape
    for i in range(n_rows-1):
        td = np.array(test_data[i][0:n_cols-1]).reshape(n_cols-1,1)
        a = int(test_data[:,n_cols-1][k])
        b = int(predict(model, test_x))
        #print(a,b)

        if a == b:
            j = j + 1

    rate = j / n_rows * 100
    print("right rate:%.2f%%\n"%rate)


if __name__ == "__main__":
    
    l = training()
    plt.plot(l)
    plt.show()
  ##  train_data, _, _, _, _ = nn_init()
  ##  a, b = split_train_dataset(train_data)
  ##  print(a.shape, b.shape)
  
