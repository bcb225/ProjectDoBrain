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
    parser.add_option('-u', '--userScoreFile', dest='user_score_file')
    parser.add_option('-p', '--personFile', dest='person_file')
    parser.add_option('-m', '--mobileOS', dest='mobile_os')
    parser.add_option('-j', '--jsonFile', dest='json_file')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

with open(options.person_file) as person_file:
    person_list = person_file.read().splitlines()

options = parse_commands(sys.argv[1:])

header_list = ['person_id', 'level', 'game_level','clear_date_time','Memory','VelocityPerceptual','Numerical','Discrimination','SpacePerceptual','Inference','Organizing','Creative']

rest_handler = RestHandler(mobile_os=options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.user_score_file,header_list=header_list)

f = open(options.json_file, 'w')
content_num = 0
for person_id in person_list:
    try:
        json_result = rest_handler.get_user_score_data_by_person_id(person_id)
    except:
        continue
    f.write(person_id+'\t'+json_result+'\n')
    result_dict_list = json_handler.json_user_score_data_to_dict_list(json_result,person_id, content_num)
    csv_handler.dict_to_csv(dict_list=result_dict_list)
f.close()
