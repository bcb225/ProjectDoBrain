import sys
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
    parser.add_option('-m', '--mobileOS', dest='mobile_os')
    parser.add_option('-j', '--jsonFile', dest='json_file')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])
f = open(options.json_file, 'w')

header_list = [
    'person_id', 'diagnosedDisease'
    ]

rest_handler = RestHandler(mobile_os=options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.survey_file,header_list=header_list)

json_result = rest_handler.get_survey_data()
f.write(json_result+'\n')

result_dict_list = json_handler.json_survey_data_to_dict(json_result)
csv_handler.dict_to_csv(dict_list = result_dict_list)

f.close()