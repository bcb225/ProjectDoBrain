import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from firebase_connector import FirebaseConnector
from rest_handler import RestHandler
from json_handler import JsonHandler
from csv_handler import CsvHandler

def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-i', '--inputFile', dest='input_file')
    parser.add_option('-o', '--outputFile', dest='output_file')
    parser.add_option('-p', '--personFile', dest='person_file')
    parser.add_option('-k', '--keyFile', dest='key_file' )
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

rest_handler = RestHandler()
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.output_file,header_list=header_list)

for person_id in person_list:
    json_result = rest_handler.get_json_by_person_id(person_id)
    result_dict_list = json_handler.json_to_dict_list(json_result,person_id)
    csv_handler.dict_to_csv(dict_list=result_dict_list)
    print(person_id,len(result_dict_list))


"""connector = FirebaseConnector(options.key_file)

data = connector.get_drag_data_by_person_id('000123DB-6507-424D-86A2-770DB247D396')

access_token = connector.get_access_token()

data_via = connector.get_drag_data_by_person_id_with_access_token('000123DB-6507-424D-86A2-770DB247D396')

print(data)
print(access_token)
print(data_via)"""