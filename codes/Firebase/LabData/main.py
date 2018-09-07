import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rest_handler import RestHandler
from json_handler import JsonHandler
from csv_handler import CsvHandler

def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-o', '--labFile', dest='lab_file')
    parser.add_option('-p', '--personFile', dest='person_file')
    parser.add_option('-m', '--mobileOs', dest='mobile_os')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

with open(options.person_file) as person_file:
    person_list = person_file.read().splitlines()

options = parse_commands(sys.argv[1:])

header_list = [
    "person_id", "todayMissionChapterButtonIndexes","dateTimeForMonth",
    "dateTimeForWeek", "dateTimeForToday", "monthTotalMissionCount",
    "monthClearMissionCount", "weekClearMissionCount", "todayClearMissionCount",
    "updateDateTime", "startDateTime", "weekIndex","velocityPerceptualPoint","memoryPoint",
    "creativePoint", "spacePerceptualPoint", "numericalPoint", "discriminationPoint",
    "inferencePoint", "organizingPoint"
    ]

rest_handler = RestHandler(mobile_os=options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.lab_file,header_list=header_list)

for person_id in person_list:
    try:
        json_result = rest_handler.get_lab_data_by_person_id(person_id)
        result_dict_list = json_handler.json_lab_data_to_dict_list(json_result, person_id)
        csv_handler.dict_to_csv(dict_list=result_dict_list)
        print(person_id,len(result_dict_list))
    except:
        print(person_id, 'EXCEPTION')