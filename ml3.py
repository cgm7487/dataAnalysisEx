import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans


dataSetX = []
random_state = 170

import csv
with open('learn_data2.csv', newline='') as csvfile:
	carReader = csv.reader(csvfile, delimiter=',')
	for row in carReader:
		dataSetX.append(list(map(float, row[0:3])))

arrayX = np.asarray(dataSetX)

y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(arrayX)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(arrayX[:, 0], arrayX[:, 1], arrayX[:, 2], c= y_pred)

plt.title('RPM&Fuel&Speed k-mean')

plt.show()

#plt.subplot(221)
#plt.scatter(arrayX[:, 1], arrayX[:, 0], c=y_pred)
#plt.title("RPM&Fuel")

#plt.subplot(223)
#plt.scatter(arrayX[:, 1], arrayX[:, 2], c=y_pred)
#plt.title("Speed&Fuel")

plt.show()

