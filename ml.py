#import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

dataSetXTrain = []
dataSetXTest = []

dataSetYTrain = []
dataSetYTest = []

dataIndex = 0

import csv
with open('cardata.csv', newline='') as csvfile:
	carReader = csv.reader(csvfile, delimiter=',')
	for row in carReader:
		if dataIndex < 50:
			dataSetXTrain.append(list(map(float, row[0:3])))
			dataSetYTrain.append(float(row[3]))
		if dataIndex >= 50:
			dataSetXTest.append(list(map(float, row[0:3])))
			dataSetYTest.append(float(row[3]))
		dataIndex += 1

regr = linear_model.LinearRegression()

regr.fit(dataSetXTrain, dataSetYTrain)


print("Mean squared error: %.2f"
      % np.mean((regr.predict(dataSetXTest) - dataSetYTest) ** 2))

print('Variance score: %.2f' % regr.score(dataSetXTest, dataSetYTest))
