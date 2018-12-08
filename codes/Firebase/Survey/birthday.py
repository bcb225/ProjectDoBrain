import sys
import json
import pandas as pd
from os.path import expanduser
home = expanduser("~")
sys.path.append('{}/ProjectDoBrain/codes/Modules'.format(home))
from rest_handler import RestHandler
from json_handler import JsonHandler
from csv_handler import CsvHandler

def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-s', '--surveyFile', dest='survey_file')
    parser.add_option('-b', '--birthdayFile', dest='birthday_file')
    parser.add_option('-m', '--mobileOS', dest='mobile_os')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

header_list = [
    'person_id', 'birthday'
    ]
survey_df = pd.read_csv(options.survey_file)

rest_handler = RestHandler(mobile_os=options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.birthday_file,header_list=header_list)

for person in survey_df.person_id.unique():
    json_result = rest_handler.get_user_data_by_person_id(person)
    result_dict_list = json_handler.user_json_to_birthday(person, json_result)
    csv_handler.dict_to_csv(dict_list = result_dict_list)