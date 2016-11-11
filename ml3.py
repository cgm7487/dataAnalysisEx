import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


dataSetX = []
random_state = 170

import csv
with open('learn_data.csv', newline='') as csvfile:
	carReader = csv.reader(csvfile, delimiter=',')
	for row in carReader:
		dataSetX.append(list(map(float, row[0:4])))

arrayX = np.asarray(dataSetX)

y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(arrayX)

plt.subplot(221)
plt.scatter(arrayX[:, 0], arrayX[:, 2], c=y_pred)
plt.title("RPM&Fuel")

plt.subplot(222)
plt.scatter(arrayX[:, 1], arrayX[:, 2], c=y_pred)
plt.title("Pedal&Fuel")

plt.subplot(223)
plt.scatter(arrayX[:, 3], arrayX[:, 2], c=y_pred)
plt.title("Speed&Fuel")

plt.show()

