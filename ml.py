#import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn import svm
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import AdaBoostRegressor
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

scores = cross_val_score(regr, X = dataSetXTrain, y = dataSetYTrain)

print(scores.mean())

#print(mean_squared_error(dataSetYTest, regr.predict(dataSetXTest)))
#print("Mean squared error: %.2f"
#      % np.mean((regr.predict(dataSetXTest) - dataSetYTest) ** 2))

#print('Variance score: %.2f' % regr.score(dataSetXTest, dataSetYTest))

clf = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)

#clf.fit(dataSetXTrain, dataSetYTrain)
scores = cross_val_score(clf, X = dataSetXTrain, y = dataSetYTrain)
print(scores.mean())


#print(mean_squared_error(dataSetYTest, clf.predict(dataSetXTest)))

clf1 = DecisionTreeRegressor()
#clf1.fit(dataSetXTrain, dataSetYTrain)
scores = cross_val_score(clf1, X = dataSetXTrain, y = dataSetYTrain)
print(scores.mean())

#print(mean_squared_error(dataSetYTest, clf1.predict(dataSetXTest)))

clf2 = RandomForestRegressor()

#clf2.fit(dataSetXTrain, dataSetYTrain)

scores = cross_val_score(clf2, X = dataSetXTrain, y = dataSetYTrain)
print(scores.mean())

clf3 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4),
                          n_estimators=300, random_state=np.random.RandomState(1))

#clf2.fit(dataSetXTrain, dataSetYTrain)

scores = cross_val_score(clf3, X = dataSetXTrain, y = dataSetYTrain)
print(scores.mean())

#print(mean_squared_error(dataSetYTest, clf2.predict(dataSetXTest)))

#print(clf.predict(dataSetXTest))

#print("Mean squared error: %.2f"
#      % np.mean((clf.predict(dataSetXTest) - dataSetYTest) ** 2))

#print('Variance score: %.2f' % clf.score(dataSetXTest, dataSetYTest))
