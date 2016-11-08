#import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
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
		dataSetYTrain.append(float(row[3]))
		#if dataIndex >= boundary:
			#dataSetXTest.append(list(map(float, row[0:3])))
			#dataSetYTest.append(float(row[3]))
		#dataIndex += 1

regr = linear_model.LinearRegression()

#regr.fit(dataSetXTrain, dataSetYTrain)

scores = cross_val_score(regr, dataSetXTrain, dataSetYTrain, scoring='neg_mean_squared_error')

print(scores.mean())

#print(mean_squared_error(dataSetYTest, regr.predict(dataSetXTest)))
#print("Mean squared error: %.2f"
#      % np.mean((regr.predict(dataSetXTest) - dataSetYTest) ** 2))

#print('Variance score: %.2f' % regr.score(dataSetXTest, dataSetYTest))

clf = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)

#clf.fit(dataSetXTrain, dataSetYTrain)
scores = cross_val_score(clf, dataSetXTrain, dataSetYTrain, scoring='neg_mean_squared_error')
print(scores.mean())


#print(mean_squared_error(dataSetYTest, clf.predict(dataSetXTest)))

clf1 = tree.DecisionTreeRegressor()
#clf1.fit(dataSetXTrain, dataSetYTrain)
scores = cross_val_score(clf1, dataSetXTrain, dataSetYTrain, scoring='neg_mean_squared_error')
print(scores.mean())

#print(mean_squared_error(dataSetYTest, clf1.predict(dataSetXTest)))

#clf2 = RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)

#clf2.fit(dataSetXTrain, dataSetYTrain)

#print(mean_squared_error(dataSetYTest, clf2.predict(dataSetXTest)))

#print(clf.predict(dataSetXTest))

#print("Mean squared error: %.2f"
#      % np.mean((clf.predict(dataSetXTest) - dataSetYTest) ** 2))

#print('Variance score: %.2f' % clf.score(dataSetXTest, dataSetYTest))
