import http.client
import json
import ast

DATA_UPPER_BOUND = [2000, 255, 10000, 40, 'str', 'str', 40, 0]

conn = http.client.HTTPSConnection("obd2cloud.apps.exosite.io")
conn.request("GET", "/development/device/moredata?device=als7061&limit=120")
r1 = conn.getresponse()
data1 = r1.read()

dataString = data1.decode(encoding='UTF-8')
jsonObj = json.loads(dataString)

import csv
with open('cardata.csv', 'w', newline='') as csvfile:
    dataWriter = csv.writer(csvfile, delimiter=',')
	
    dataHeader = []
    for i in range(8):
        dataHeader.append(jsonObj['timeseries']['results'][0]['series'][i]['name'])
    dataWriter.writerow(dataHeader)
    
    for i in range(120):
        rowData = []
        needToSaveData = True
        for j in range(8):
            if type(DATA_UPPER_BOUND[j]) == type(1):
                if jsonObj['timeseries']['results'][0]['series'][j]['values'][i][1] == 'NODATA' or float(jsonObj['timeseries']['results'][0]['series'][j]['values'][i][1]) > DATA_UPPER_BOUND[j]:
                    needToSaveData = False
                    continue
            rowData.append(jsonObj['timeseries']['results'][0]['series'][j]['values'][i][1])

        if needToSaveData:
            dataWriter.writerow(rowData)
