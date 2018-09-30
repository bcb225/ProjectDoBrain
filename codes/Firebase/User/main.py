import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rest_handler import RestHandler
from json_handler import JsonHandler
from csv_handler import CsvHandler

def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-o', '--userFile', dest='user_file')
    parser.add_option('-p', '--personFile', dest='person_file')
    parser.add_option('-m', '--mobileOS', dest='mobile_os')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

with open(options.person_file) as person_file:
    person_list = person_file.read().splitlines()

options = parse_commands(sys.argv[1:])

header_list = ['person_id', 'level']

rest_handler = RestHandler(mobile_os=options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.user_file,header_list=header_list)

for person_id in person_list:
    json_result = rest_handler.get_user_data_by_person_id(person_id)
    result_dict_list = json_handler.json_user_data_to_dict_list(json_result,person_id)
    print(result_dict_list)
    csv_handler.dict_to_csv(dict_list=result_dict_list)