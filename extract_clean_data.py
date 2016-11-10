import http.client
import json
import ast

DATA_UPPER_BOUND = [2000, 255, 10000, 'str', 656, 100, 'str','str', 'str', 40, 100]

NUM_OF_DATA = 250

conn = http.client.HTTPSConnection("obd2cloud.apps.exosite.io")
conn.request("GET", "/development/device/moredata?device=als7061&limit="+str(NUM_OF_DATA))
r1 = conn.getresponse()
data1 = r1.read()

dataString = data1.decode(encoding='UTF-8')
jsonObj = json.loads(dataString)

import csv
with open('cardata2.csv', 'w', newline='') as csvfile:
    dataWriter = csv.writer(csvfile, delimiter=',')
	
    dataHeader = []
    for i in range(11):
        dataHeader.append(jsonObj['timeseries']['results'][0]['series'][i]['name'])
    dataWriter.writerow(dataHeader)
    
    for i in range(NUM_OF_DATA):
        rowData = []
        needToSaveData = True
        for j in range(11):
            if type(DATA_UPPER_BOUND[j]) == type(1):
                if jsonObj['timeseries']['results'][0]['series'][j]['values'][i][1] == 'NODATA' or float(jsonObj['timeseries']['results'][0]['series'][j]['values'][i][1]) > DATA_UPPER_BOUND[j]:
                    needToSaveData = False
                    continue
            rowData.append(jsonObj['timeseries']['results'][0]['series'][j]['values'][i][1])

        if needToSaveData:
            dataWriter.writerow(rowData)
