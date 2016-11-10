#import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn import svm
from sklearn import tree
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score

dataSetXTrain = []
#dataSetXTest = []

dataSetYTrain = []
#dataSetYTest = []

dataIndex = 0

boundary = 40

import csv
with open('learn_data.csv', newline='') as csvfile:
	carReader = csv.reader(csvfile, delimiter=',')
	for row in carReader:
		#if dataIndex < boundary:
		dataSetXTrain.append(list(map(float, row[0:3])))
		dataSetYTrain.append(int(row[3]))
		#if dataIndex >= boundary:
			#dataSetXTest.append(list(map(float, row[0:3])))
			#dataSetYTest.append(float(row[3]))
		#dataIndex += 1

clf = svm.SVC()

#clf.fit(dataSetXTrain, dataSetYTrain)
scores = cross_val_score(clf, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())


clf1 = tree.DecisionTreeClassifier()
#clf1.fit(dataSetXTrain, dataSetYTrain)
scores = cross_val_score(clf1, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())

#print(mean_squared_error(dataSetYTest, clf1.predict(dataSetXTest)))

clf2 = RandomForestClassifier(n_estimators=10)

#clf2.fit(dataSetXTrain, dataSetYTrain)
scores = cross_val_score(clf2, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())

clf3 = AdaBoostClassifier(n_estimators=100)

#clf3.fit(dataSetXTrain, dataSetYTrain)
scores = cross_val_score(clf3, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())

clf4 = neighbors.KNeighborsClassifier(15, weights='distance')

scores = cross_val_score(clf4, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())

gnb = GaussianNB()
scores = cross_val_score(gnb, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())

#print(mean_squared_error(dataSetYTest, clf2.predict(dataSetXTest)))

#print(clf.predict(dataSetXTest))

#print("Mean squared error: %.2f"
#      % np.mean((clf.predict(dataSetXTest) - dataSetYTest) ** 2))

#print('Variance score: %.2f' % clf.score(dataSetXTest, dataSetYTest))
