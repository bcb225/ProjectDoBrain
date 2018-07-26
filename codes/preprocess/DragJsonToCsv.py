import json
import sys 
import csv
dragFileName = sys.argv[1]
csvFileName = sys.argv[2]
with open(dragFileName) as f:
    jsonData = json.load(f)
csvFile = open(csvFileName, "wb")
csvWriter = csv.writer(csvFile, delimiter = ',')
csvWriter.writerow(
                            ["person","updateDateTime","screenHeight","screenWidth",
                            "contentIndex", "questionIndex", "derivedQuestionIndex","dragDataSetCreationDateTime",
                            "dragDataCreationDateTime", "isOnCorrectAnswer","posX","posY", "touchPressure"
                            ]
                        )
for person in jsonData:
    i = 0
    try:
        updateDateTime = jsonData[person]["_updateDateTime"]
    except:
        updateDateTime = "N/A"
    screenHeight = jsonData[person]["_screenHeight"]
    screenWidth = jsonData[person]["_screenWidth"]
    contentDragData = jsonData[person]["contentDragData"]
    
    for contentDragDatum in contentDragData:
        contentIndex = contentDragDatum["_index"]
        questionDragData = contentDragDatum["questionDragData"]
        for questionDragDatum in questionDragData:
            questionIndex = questionDragDatum["_index"]
            derivedQuestionDragData = questionDragDatum["derivedQuestionDragData"]
            for derivedQuestionDragDatum in derivedQuestionDragData:
                derivedQuestionIndex = derivedQuestionDragDatum["_index"]
                dragDataSets = derivedQuestionDragDatum["dragDataSets"]
                for dragDataSet in dragDataSets:
                    dragDataSetCreationDateTime = dragDataSet["creationDateTime"]
                    try:
                        dragData = dragDataSet["dragData"]
                    except:
                        dragData = ""
                    for dragDatum in dragData:
                        dragDataCreationDateTime = dragDatum["creationDateTime"]
                        isOnCorrectAnswer = dragDatum["isOnCorrectAnswer"]
                        posX = dragDatum["posX"]
                        posY = dragDatum["posY"]
                        touchPressure = dragDatum["touchPressure"]
                        csvWriter.writerow(
                            [person,updateDateTime,screenHeight,screenWidth,
                            contentIndex, questionIndex, derivedQuestionIndex,dragDataSetCreationDateTime,
                            dragDataCreationDateTime, isOnCorrectAnswer,posX,posY, touchPressure
                            ]
                        )
                        #print(person,updateDateTime, screenHeight, screenWidth,contentIndex, dragDatum["touchPressure"])
    #print("%s\n %s" % (person, updateDateTime))