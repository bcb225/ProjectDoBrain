import csv
import sys 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
csvFileName = sys.argv[1]
csvFile = open(csvFileName, "r")
csvReader = csv.reader(csvFile, delimiter = ',')
rowDict = {}
personDragDict = {}
for row in csvReader:
    header = ['person','updateDateTime','screenHeight','screenWidth',
                            'contentIndex', 'questionIndex', 'derivedQuestionIndex','dragDataSetCreationDateTime',
                            'dragDataCreationDateTime', 'isOnCorrectAnswer','posX','posY', 'touchPressure']
    for index, item in enumerate(header):
        rowDict[item] = row[index]
    if rowDict['contentIndex'] == "1" and rowDict['questionIndex'] == "6" and rowDict['derivedQuestionIndex'] == "0":
        if personDragDict.has_key(rowDict['person']):
            if float(rowDict['touchPressure']) != -1 and rowDict['isOnCorrectAnswer'] == "True":
                personDragDict[rowDict['person']].append(float(rowDict['touchPressure']))
        else:
            personDragDict[rowDict['person']] = []
meanTouchPressureList = []
for eachItem in personDragDict:
    print(eachItem,personDragDict[eachItem],np.mean(personDragDict[eachItem]),"\n")
    if len(personDragDict[eachItem]) > 0:
        meanTouchPressureList.append([np.mean(personDragDict[eachItem]),0])
meanTouchPressureNpArray = np.array(meanTouchPressureList)
kmeans = KMeans(n_clusters=3).fit(meanTouchPressureNpArray)
labels = kmeans.labels_
plt.scatter(meanTouchPressureNpArray[:,0],meanTouchPressureNpArray[:,1],c=labels.astype(np.float))
plt.show()