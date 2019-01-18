import sys
import json
import gc
import os
import psutil
process = psutil.Process(os.getpid())
from os.path import expanduser
home = expanduser("~")

sys.path.append('{}/ProjectDoBrain/codes/Modules'.format(home))
from rest_handler import RestHandler
from json_handler import JsonHandler
from csv_handler import CsvHandler

def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-o', '--dragFile', dest='drag_file')
    parser.add_option('-j', '--jsonFile', dest='json_file')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

header_list = ["person_id","deviceModel","deviceName","dpi", "updateDateTime", "screenHeight", "screenWidth",
                "level", "contentIndex", "questionIndex", "derivedQuestionIndex",
                "questionManagerCategory", "dragDataSetCreationDateTime",
                "dragDataCreationDateTime", "isOnCorrectAnswer", 
                "posX", "posY", "touchPressure"
                ]

rest_handler = RestHandler()
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.drag_file,header_list=header_list)

#f = open(options.json_file, 'w')
date_list_json = rest_handler.get_json_of_date_list()
date_list = json_handler.json_to_date_list(date_list_json)
survey_person_list = []
for mobile_os in ('iOS','Android'):
    survey_rest_handler = RestHandler(mobile_os=mobile_os)
    survey_json = survey_rest_handler.get_survey_data()
    temp_person_list = json_handler.json_survey_data_to_person_list(survey_json)
    survey_person_list += temp_person_list
survey_person_set = set(survey_person_list)
survey_person_set.add('3c234013d1ec58644fe3779b67542e45')
survey_person_set.add('48f116a8d36c91fa878653d625b75102')
survey_person_set.add('ac3af7c24fb5dd6a21246fb8d3203a1f')
survey_person_set.add('9e50490e225486262f37e2a9f220d7da')
survey_person_set.add('4ea63ce37fafb10cc4a66ea0e5f42bdd')

for idx, date in enumerate(date_list):
#for idx, date in enumerate(['1970-01-01','2019-02-07']):
    #result_dict_list = []
    if date == '1970/01/01':
        print('Date 1970/01/01')
        continue
    print('[{}], ({}/{}) Now Collecting'.format(date,idx+1,len(date_list)))
    for mobile_os in ('iOS', 'Android'):
        person_list_json = rest_handler.get_json_of_person_id_by_date(date,mobile_os)
        person_list = json_handler.json_to_person_list(person_list_json,mobile_os)
        all_person_set = set(person_list)
        updated_person_set = all_person_set.intersection(survey_person_set)
        updated_person_list = list(updated_person_set)
        print('\t\tAll {} users : {}, Survey {} users {}'.format(mobile_os,len(person_list),mobile_os,len(updated_person_list)))
        for person_id in updated_person_list:
            drag_data_json = rest_handler.get_json_by_date_and_person_id(date,person_id,mobile_os)
            temp_dict_list = json_handler.json_to_dict_list(json_source = drag_data_json,person_id =person_id)
            #result_dict_list += temp_dict_list
            csv_handler.dict_to_csv(temp_dict_list)
    #del result_dict_list
    #print(process.memory_info().rss)  # in bytes 
    #gc.collect()