import json

class JsonHandler:
    def __init__(self):
        pass
    
    def json_to_dict_list(self,json_source,person_id):
        json_text = json.dumps(json_source)
        json_data = json.loads(json_text)
        result_dict_list = []
        try:
            updateDateTime = json_data['_updateDateTime']
        except:
            updateDateTime = 'N/A'
        screenHeight = json_data['_screenHeight']
        screenWidth = json_data['_screenWidth']

        try:
            userLevels = json_data['_userLevels']
            for userLevel in userLevels:
                level = userLevel['_level']
                contentDragData = userLevel['contentDragData']
                temp_dict_list = self.contentDragData_parser(contentDragData,updateDateTime,screenHeight,screenWidth,level,person_id)
                result_dict_list = result_dict_list + temp_dict_list
        
        except:
            level = 'N/A'
            contentDragData = json_data['contentDragData']
            result_dict_list = self.contentDragData_parser(contentDragData,updateDateTime,screenHeight,screenWidth,level,person_id)
        return result_dict_list
    def contentDragData_parser(self,contentDragData,updateDateTime,screenHeight,screenWidth,level,person_id):
        result_dict_list = []
        for contentDragDatum in contentDragData:
            contentIndex = contentDragDatum["_index"]
            questionDragData = contentDragDatum["questionDragData"]
            for questionDragDatum in questionDragData:
                questionIndex = questionDragDatum["_index"]
                derivedQuestionDragData = questionDragDatum["derivedQuestionDragData"]
                try:
                    questionManagerCategory = questionDragDatum['_questionManagerCategory']
                except:
                    questionManagerCategory = 'N/A'
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
                            temp_dict = {
                                "person_id" : person_id,
                                "updateDateTime" : updateDateTime,
                                "screenHeight" : screenHeight,
                                "screenWidth" : screenWidth,
                                "level" : level,
                                "contentIndex" : contentIndex,
                                "questionIndex" : questionIndex,
                                "derivedQuestionIndex" : derivedQuestionIndex,
                                "questionManagerCategory" : questionManagerCategory,
                                "dragDataSetCreationDateTime" : dragDataSetCreationDateTime,
                                "dragDataCreationDateTime" : dragDataCreationDateTime,
                                "isOnCorrectAnswer" : isOnCorrectAnswer,
                                "posX" : posX,
                                "posY" : posY,
                                "touchPressure" : touchPressure
                            }
                            result_dict_list.append(temp_dict)
        return result_dict_list