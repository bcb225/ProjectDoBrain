import json
import regex as re
import datetime
import dateutil.parser
from pprint import pprint
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
            deviceModel = json_data['_deviceModel']
        except:
            deviceModel = ""

        try:
            deviceName = json_data['_deviceName']
        except:
            deviceName = ""
        try:
            dpi = json_data['_dpi']
        except:
            dpi = ""
        try:
            userLevels = json_data['_userLevels']
            for userLevel in userLevels:
                level = userLevel['_level']
                contentDragData = userLevel['contentDragData']
                temp_dict_list = self.contentDragData_parser(contentDragData,updateDateTime,screenHeight,screenWidth,level,person_id,deviceModel,deviceName,dpi)
                result_dict_list = result_dict_list + temp_dict_list
        
        except:
            level = 'N/A'
            contentDragData = json_data['contentDragData']
            result_dict_list = self.contentDragData_parser(contentDragData,updateDateTime,screenHeight,screenWidth,level,person_id,deviceModel,deviceName,dpi)
        return result_dict_list
    def contentDragData_parser(self,contentDragData,updateDateTime,screenHeight,screenWidth,level,person_id,deviceModel,deviceName,dpi):
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
                                "deviceModel" : deviceModel,
                                "deviceName" : deviceName,
                                "dpi" : dpi,
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
    
    def json_to_person_list(self, json_source, mobile_os):
        result_list = []
        try:
            if mobile_os == 'iOS':
                json_data = json.loads(json_source)
                person_id_list = json_data.keys()
                p = re.compile('\w+\-\w+\-\w+\-\w+\-\w+')
                for elm in person_id_list:
                    result_list.append(elm)
            elif mobile_os == 'Android':
                json_data = json.loads(json_source)
                person_id_list = json_data.keys()
                for person_id in person_id_list:
                    result_list.append(person_id)
        except:
            pass
        return result_list

    def json_to_date_list(self,json_source):
        json_data = json.loads(json_source)
        date_list = list(json_data.keys())
        return date_list
            
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
    def json_user_score_data_to_dict_list(self, json_source, person_id, content_num):
        json_data = json.loads(json_source)
        result_dict_list = []
        score_name_list = ['Memory','VelocityPerceptual','Numerical','Discrimination','SpacePerceptual','Inference','Organizing','Creative']
        score_name_list_set = set(score_name_list)
        category_list = []
        try:
            level = json_data['level']
            userContentsDatum = json_data['userContentsData']
            contentData = userContentsDatum[content_num]
            clearDateTimes = contentData['clearDateTimes']
            first_time = clearDateTimes[0]
            parsed_first_time = dateutil.parser.parse(first_time)
            
            userQuestionDatum = contentData['userQuestionData']
            score_list = []
            for userQuestionData in userQuestionDatum:
                point_list = []
                category = userQuestionData['categories'][0]
                category_list.append(category)
                if category == '':
                    return result_dict_list
                userDerivedQuestionDatum = userQuestionData['userDerivedQuestionData']
                for userDerivedQuestionData in userDerivedQuestionDatum:
                    game_time = userDerivedQuestionData['clearDateTime']
                    parsed_game_time = dateutil.parser.parse(game_time)
                    if parsed_game_time <= parsed_first_time:
                        point = userDerivedQuestionData['point']
                        game_level = userDerivedQuestionData['level']
                        point_list.append(point)
                        
                
                avg_point = sum(point_list)/len(point_list)
                
                score_list.append([category, avg_point])
            
            category_list_set = set(category_list)
            if category_list_set != score_name_list_set:
                print(person_id + ' ABORTED(different score list)' +category_list)
                return result_dict_list
            if len(score_list) != 8:
                print(person_id + ' ABORTED(less score list)')
                return result_dict_list
            temp_dict = {
                'person_id' : person_id,
                'level' : level,
                'game_level' : game_level,
                'clear_date_time' : first_time
            }
            for score in score_list:
                temp_dict[score[0]] = score[1]
            
            result_dict_list.append(temp_dict)
            print(person_id + ' COMPLETED')
            return result_dict_list
        except Exception as e:
            print(person_id + ' ABORTED(cannot locate)'+str(e))
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
            wonDiagnosis = person_survey['wonDiagnosis']
            if wonDiagnosis == '없다' or wonDiagnosis == 'No':
                temp_dict = {
                    'person_id' : person_id,
                    'wonDiagnosis' : 'N/A',
                    'worryingCategory' : 'N/A',
                    'diagnosedDisease' : 'N/A'
                }
                result_dict_list.append(temp_dict)
            elif wonDiagnosis == '진단받은 적은 없으나, 염려된다' or wonDiagnosis == 'No, but I\'m worried':
                worryingCategories = person_survey['worryingCategories']
                print(worryingCategories)
                for worryingCategory in worryingCategories:
                    temp_dict = {
                        'person_id' : person_id,
                        'wonDiagnosis' : 'Worry',
                        'worryingCategory' : worryingCategory,
                        'diagnosedDisease' : 'N/A'
                    }
                    result_dict_list.append(temp_dict)
            elif wonDiagnosis == '있다' or wonDiagnosis == 'Yes':
                diagnosedDiseases = person_survey['diagnosedDiseases']
                for diagnosedDisease in diagnosedDiseases:
                    diagnosedDisease = diagnosedDisease
                    temp_dict = {
                        'person_id' : person_id,
                        'wonDiagnosis' : 'Diagnosed',
                        'worryingCategory' : 'N/A',
                        'diagnosedDisease' : diagnosedDisease
                    }
                    result_dict_list.append(temp_dict)
            else:
                print(wonDiagnosis)
            
        return result_dict_list

    def user_json_to_birthday(self, person_id,json_source):
        result_dict_list = []
        json_data = json.loads(json_source)
        birthday = json_data['birthday']
        temp_dict = {
                'person_id' : person_id,
                'birthday' : birthday
            }
        result_dict_list.append(temp_dict)

        return result_dict_list