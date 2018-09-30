import json
import regex as re
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
    def json_lab_data_to_dict_list(self, json_source, person_id):
        json_text = json.dumps(json_source)
        json_data = json.loads(json_text)
        result_dict_list = []
        try :
            todayMissionChapterButtonIndexes = json_data['todayMissionChapterButtonIndexes']
        except:
            todayMissionChapterButtonIndexes = 'N/A'
        dateTimeForWeek = json_data['dateTimeForWeek']
        weekClearMissionCount = json_data['weekClearMissionCount']
        dateTimeForMonth = json_data['dateTimeForMonth']
        todayClearMissionCount= json_data['todayClearMissionCount']
        kidsLabWeekData = json_data['kidsLabWeekData']
        monthClearMissionCount = json_data['monthClearMissionCount']
        monthTotalMissionCount = json_data['monthTotalMissionCount']
        updateDateTime = json_data['updateDateTime']
        dateTimeForToday = json_data['dateTimeForToday']
        for kidsLabWeekDatum in kidsLabWeekData:
            velocityPerceptualPoint = kidsLabWeekDatum['velocityPerceptualPoint']
            memoryPoint = kidsLabWeekDatum['memoryPoint']
            startDateTime = kidsLabWeekDatum['startDateTime']
            creativePoint = kidsLabWeekDatum['creativePoint']
            weekIndex = kidsLabWeekDatum['weekIndex']
            spacePerceptualPoint = kidsLabWeekDatum['spacePerceptualPoint']
            numericalPoint = kidsLabWeekDatum['numericalPoint']
            discriminationPoint = kidsLabWeekDatum['discriminationPoint']
            inferencePoint = kidsLabWeekDatum['inferencePoint']
            try :
                organizingPoint = kidsLabWeekDatum['organizingPoint']
            except:
                organazingPoint = kidsLabWeekDatum['organazingPoint']
                organizingPoint = organazingPoint
            temp_dict = {
                        "person_id" : person_id,
                        "todayMissionChapterButtonIndexes" : todayMissionChapterButtonIndexes,
                        "dateTimeForMonth" : dateTimeForMonth,
                        "dateTimeForWeek" : dateTimeForWeek,
                        "dateTimeForToday" : dateTimeForToday,
                        "monthTotalMissionCount" : monthTotalMissionCount,
                        "monthClearMissionCount" : monthClearMissionCount,
                        "weekClearMissionCount" : weekClearMissionCount,
                        "todayClearMissionCount" : todayClearMissionCount,
                        
                        "updateDateTime" : updateDateTime,
                        
                        "weekIndex" : weekIndex,
                        "velocityPerceptualPoint" : velocityPerceptualPoint,
                        "memoryPoint" : memoryPoint,
                        "startDateTime" : startDateTime,
                        "creativePoint" : creativePoint,
                        "spacePerceptualPoint" : spacePerceptualPoint,
                        "numericalPoint" : numericalPoint,
                        "discriminationPoint" : discriminationPoint,
                        "inferencePoint" : inferencePoint,
                        "organizingPoint" : organizingPoint
                    }
            result_dict_list.append(temp_dict)
        return result_dict_list
    def json_person_id_to_dict_list(self, json_source, mobile_os):
        result_dict_list = []        
        if mobile_os == 'iOS':
            json_data = json.loads(json_source)
            person_id_list = json_data.keys()
            p = re.compile('\w+\-\w+\-\w+\-\w+\-\w+')
            for elm in person_id_list:
                if p.match(elm):
                    temp_dict = {
                        "person_id" : elm
                    }
                    result_dict_list.append(temp_dict)
        elif mobile_os == 'Android':
            json_data = json.loads(json_source)
            person_id_list = json_data.keys()
            for person_id in person_id_list:
                temp_dict = {
                    "person_id" : person_id
                }
                result_dict_list.append(temp_dict)
        return result_dict_list
    
    def json_user_data_to_dict_list(self, json_source, person_id):
        json_data = json.loads(json_source)
        result_dict_list = []
        try :
            level = json_data['level']
        
            temp_dict ={
                'person_id' : person_id,
                'level' : level
            }

            result_dict_list.append(temp_dict)

            return result_dict_list

        except:
            return result_dict_list

    def json_lesson_bucket_data_to_dict_list(self, json_source, index):
        json_text = json.dumps(json_source)
        json_data = json.loads(json_text)
        A_result_dict_list = []
        B_result_dict_list = []
        C_result_dict_list = []

        level = json_data['level']
        try:
            A_result_dict_list = self.lesson_bucket_level_parser(
            level_dict = level, target_level = 'A', index = index
            )
        except:
            pass
        
        try:
            B_result_dict_list = self.lesson_bucket_level_parser(
            level_dict = level, target_level = 'B', index = index
            )
        except:
            pass
        
        try:
            C_result_dict_list = self.lesson_bucket_level_parser(
            level_dict = level, target_level = 'C', index = index
            )
        except:
            pass
        
        total_result_dict_list = A_result_dict_list + B_result_dict_list + C_result_dict_list
        print(total_result_dict_list)
        return total_result_dict_list

    def lesson_bucket_level_parser(self, level_dict,target_level,index):
        result_dict_list = []
        level = level_dict[target_level]
        categories = level['categories']
        
        attentionMemory = categories['attentionMemory']
        attentionMemoryUsers = attentionMemory['users']
        
        constructionalAbility = categories['constructionalAbility']
        constructionalAbilityUsers = constructionalAbility['users']

        discernment = categories['discernment']
        discernmentUsers = discernment['users']

        logicalReasoning = categories['logicalReasoning']
        logicalReasoningUsers = logicalReasoning['users']

        mathematicalThinking = categories['mathematicalThinking']
        mathematicalThinkingUsers = mathematicalThinking['users']

        reaction = categories['reaction']
        reactionUsers = reaction['users']

        spatialPerception = categories['spatialPerception']
        spatialPerceptionUsers = spatialPerception['users']
        
        attentionMemoryKeySet = set(attentionMemoryUsers.keys())
        constructionalAbilityKeySet = set(constructionalAbilityUsers.keys())
        discernmentKeySet = set(discernmentUsers.keys())
        logicalReasoningKeySet = set(logicalReasoningUsers.keys())
        mathematicalThinkingKeySet = set(mathematicalThinkingUsers.keys())
        reactionKeySet = set(reactionUsers.keys())
        spatialPerceptionKeySet = set(spatialPerceptionUsers.keys())

        intersection_keys = attentionMemoryKeySet.intersection(
            constructionalAbilityKeySet.intersection(
                discernmentKeySet.intersection(
                    logicalReasoningKeySet.intersection(
                        mathematicalThinkingKeySet.intersection(
                            reactionKeySet.intersection(
                                spatialPerceptionKeySet
                            )
                        )
                    )
                )
            )
        )

        for key in intersection_keys:
            temp_dict = {
                        "index" : index,
                        "person_id" : key,
                        "level" : target_level,
                        "attentionMemory" : attentionMemoryUsers[key],
                        "constructionalAbility" : constructionalAbilityUsers[key],
                        "discernment" : discernmentUsers[key],
                        "logicalReasoning" : logicalReasoningUsers[key],
                        "mathematicalThinking" : mathematicalThinkingUsers[key],
                        "reaction" : reactionUsers[key],
                        "spatialPerception" : spatialPerceptionUsers[key]
                    }
            result_dict_list.append(temp_dict)
        return(result_dict_list)

    def json_survey_data_to_dict(self, json_source):
        result_dict_list = []
        json_text = json.dumps(json_source)
        json_data = json.loads(json_text)
        for person_id in json_data:
            person_survey = json_data[person_id]
            try :
                diagnosedDiseases = person_survey['diagnosedDiseases']
                print(diagnosedDiseases)
                for diagnosedDisease in diagnosedDiseases:
                    utf8_diagnosedDisease = diagnosedDisease.encode("utf-8")
                    temp_dict = {
                        'person_id' : person_id,
                        'diagnosedDisease' : utf8_diagnosedDisease
                    }
                    print(utf8_diagnosedDisease)
                    result_dict_list.append(temp_dict)
            except:
                temp_dict = {
                        'person_id' : person_id,
                        'diagnosedDisease' : 'N/A'
                    }
                result_dict_list.append(temp_dict)
        return result_dict_list