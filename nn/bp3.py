from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from matplotlib import pyplot as plt
import pandas
# 引入数据
def data_init():
	datasets = np.loadtxt('mess2.csv', delimiter=',')
	X_train, X_test, = train_test_split(datasets,test_size=0.3)
	return X_train, X_test

# 将数据中的Y值分割出来
def split_data(x):
	x1 = x[:,0:x.shape[1]-1]
	x2 = x[:,-1]
	return x1, x2

def train(X_tr, X_te):
	X_train, y_train = split_data(X_tr)
	m = MinMaxScaler()
	X_train = m.fit_transform(X_train)

	X_test, y_test = split_data(X_te)
	X_test = m.fit_transform(X_test)
	clf = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-5, hidden_layer_sizes=(1),learning_rate_init=.01)

	clf.fit(X_train, y_train)

	y_pred = clf.predict(X_test)

	print(classification_report(y_test, y_pred))
	#return clf.score(X_test, y_test)
	# print(clf.n_layers_)
	return clf.loss_
	# print(clf.out_activation_)
	
	'''
	precision：关注于所有被预测为正（负）的样本中究竟有多少是正（负）。
	predicted:关注于所有真实为正（负）的样本有多少被准确预测出来
	f1-score：二者均值。
	supprot：每个标签的出现次数。	
	'''
def test():
	
	e = []
	X_tr, X_te = data_init()
	
	for i in range(100):		
		e.append(train(X_tr, X_te))		
	# plt.plot(e)
	# plt.show()

if __name__ == '__main__':
	test()
