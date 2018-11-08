import sys
import re
from os.path import expanduser
home = expanduser("~")
sys.path.append('{}/ProjectDoBrain/codes/Modules'.format(home))
from rest_handler import RestHandler
from json_handler import JsonHandler
from csv_handler import CsvHandler

def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-j', '--jsonFile', dest='json_file')
    parser.add_option('-n', '--numContent', dest='num_content')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

header_list = ['person_id', 'level', 'game_level','clear_date_time','Memory','VelocityPerceptual','Numerical','Discrimination','SpacePerceptual','Inference','Organizing','Creative']

rest_handler = RestHandler(mobile_os=options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.user_score_file,header_list=header_list)


for i in range(0,options.num_content):
    f = open(options.json_file, 'r')
    line = f.readline()
    while line:
        line_splited = re.split(r'\t',line)
        result_dict_list=json_handler.json_user_score_data_to_dict_list(line[1],line_splited[0],i)
        csv_handler.dict_to_csv(dict_list=result_dict_list)
        line = f.readline()
    f.close()
