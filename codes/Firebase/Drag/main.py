import sys
import json
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
    parser.add_option('-p', '--personFile', dest='person_file')
    parser.add_option('-m', '--mobileOS', dest='mobile_os')
    parser.add_option('-j', '--jsonFile', dest='json_file')

    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

with open(options.person_file) as person_file:
    person_list = person_file.read().splitlines()

header_list = ["person_id", "updateDateTime", "screenHeight", "screenWidth",
                "level", "contentIndex", "questionIndex", "derivedQuestionIndex",
                "questionManagerCategory", "dragDataSetCreationDateTime",
                "dragDataCreationDateTime", "isOnCorrectAnswer", 
                "posX", "posY", "touchPressure"
                ]

rest_handler = RestHandler(options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.drag_file,header_list=header_list)

f = open(options.json_file, 'w')
for person_id in person_list:
    try:
        json_result = rest_handler.get_json_by_person_id(person_id)
        f.write(json.dumps(json_result)+'\n')
        result_dict_list = json_handler.json_to_dict_list(json_result,person_id)
        csv_handler.dict_to_csv(dict_list=result_dict_list)
        print(person_id,len(result_dict_list))
    except:
        print('EXCEPTION',person_id)
        pass