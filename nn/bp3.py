from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve
from matplotlib import pyplot as plt

import numpy as np
import pandas

# 引入数据
def data_init():
	datasets = np.loadtxt('mess.csv', delimiter=',')
	X_train, X_test = train_test_split(datasets, test_size=0.3)
	return X_train, X_test

# 将数据中的Y值分割出来
def split_data(x):
	x1 = x[:, 0:x.shape[1]-1]
	x2 = x[:, 1]
	return x1, x2

def train(X_tr, X_te):
	X_train, y_train = split_data(X_tr)
	m = MinMaxScaler()
	X_train = m.fit_transform(X_train)
	X_test, y_test = split_data(X_te)
	X_test = m.fit_transform(X_test)
<<<<<<< HEAD
	clf = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-5, hidden_layer_sizes=(1,4),learning_rate_init=.01)

	# clf.fit(X_train, y_train)

	draw_learning_curve(clf, X_train, y_train)

	# y_pred = clf.predict(X_test)



=======
	clf = MLPClassifier(solver='lbfgs', activation='logistic', alpha=1e-5, hidden_layer_sizes=(2,3),learning_rate_init=.01)
	clf.fit(X_train, y_train)
	#draw_learning_curve(clf, X_train, y_train)
	#y_pred = clf.predict(X_test)
<<<<<<< HEAD
	print(classification_report(y_test, y_pred))
=======
>>>>>>> db07300bdb347ffa87eacc77c4be06c943f1a270
	#print(classification_report(y_test, y_pred))
>>>>>>> 61610f4dffa0efb3326a4166c6e64ee4a65e6ae2
	# return clf.score(X_test, y_test)
	# print(clf.n_layers_)
	return clf.loss_
	
	'''
	precision：关注于所有被预测为正（负）的样本中究竟有多少是正（负）。
	predicted:关注于所有真实为正（负）的样本有多少被准确预测出来
	f1-score：二者均值。
	supprot：每个标签的出现次数。	
	'''
def test():
	X_tr, X_te = data_init()
	for i in range(1):		
		train(X_tr, X_te)
	
def draw_learning_curve(pipe_lr, X_train, y_train):
	#case1：学习曲线
	#构建学习曲线评估器，train_sizes：控制用于生成学习曲线的样本的绝对或相对数量
	train_sizes, train_scores, test_scores = learning_curve(
		estimator=pipe_lr,
		X=X_train,
		y=y_train,
		train_sizes=np.linspace(0.1,1.0,10),
		cv=10,
		n_jobs=1)

	#统计结果
	train_mean = np.mean(train_scores,axis=1)
	train_std = np.std(train_scores,axis=1)
	test_mean = np.mean(test_scores,axis=1)
	test_std = np.std(test_scores,axis=1)
	#绘制效果
#	plt.plot(train_sizes, train_mean, color='blue', marker='o', markersize=5, label='training accuracy')
#	plt.fill_between(train_sizes, train_mean + train_std, train_mean - train_std, alpha=0.15, color='blue')
##	# plt.plot(train_sizes,test_mean,color='green',linestyle='--',marker='s',markersize=5,label='test accuracy')
#	# plt.fill_between(train_sizes,test_mean+test_std,test_mean-test_std,alpha=0.15,color='green')
#	plt.grid()
#	plt.xlabel('Number of training samples')
#	plt.ylabel('Accuracy')
#	plt.legend(loc='lower right')
#	plt.ylim([0.8,1.0])
#	plt.show()

if __name__ == '__main__':
	test()
