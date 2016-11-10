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
from sklearn.metrics import accuracy_score

dataSetXTrain = []
dataSetXTest = []

dataSetYTrain = []
dataSetYTest = []

dataIndex = 0

boundary = 202

import csv
with open('learn_data.csv', newline='') as csvfile:
	carReader = csv.reader(csvfile, delimiter=',')
	for row in carReader:
		if dataIndex < boundary:
			dataSetXTrain.append(list(map(float, row[0:3])))
			dataSetYTrain.append(int(int(row[3])/5))
		if dataIndex >= boundary:
			dataSetXTest.append(list(map(float, row[0:3])))
			dataSetYTest.append(int(int(row[3])/5))
		dataIndex += 1

clf1 = tree.DecisionTreeClassifier(criterion='entropy')
#clf1.fit(dataSetXTrain, dataSetYTrain)
#yPred = clf1.predict(dataSetXTest)
#print("decision tree score: {}".format(accuracy_score(dataSetYTest, yPred)))
scores = cross_val_score(clf1, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())

#print(mean_squared_error(dataSetYTest, clf1.predict(dataSetXTest)))

clf2 = RandomForestClassifier(n_estimators=20)
#clf2.fit(dataSetXTrain, dataSetYTrain)
#yPred = clf2.predict(dataSetXTest)
#print("random forest score: {}".format(accuracy_score(dataSetYTest, yPred)))
scores = cross_val_score(clf2, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())

clf3 = AdaBoostClassifier(n_estimators=100)
#clf3.fit(dataSetXTrain, dataSetYTrain)
#yPred = clf3.predict(dataSetXTest)
#print("Adaboost score: {}".format(accuracy_score(dataSetYTest, yPred)))
scores = cross_val_score(clf3, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())

clf4 = neighbors.KNeighborsClassifier(30, weights='distance')
#clf4.fit(dataSetXTrain, dataSetYTrain)
#yPred = clf4.predict(dataSetXTest)
#print("K-neighborsClassifier score: {}".format(accuracy_score(dataSetYTest, yPred)))
scores = cross_val_score(clf4, X = dataSetXTrain, y = dataSetYTrain)
print(scores)
print(scores.mean())
