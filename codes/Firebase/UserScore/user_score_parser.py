import sys
import re
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
    parser.add_option('-j', '--jsonFile', dest='json_file')
    parser.add_option('-n', '--numContent', dest='num_content')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

header_list = ['person_id', 'level', 'game_level','clear_date_time','Memory','VelocityPerceptual','Numerical','Discrimination','SpacePerceptual','Inference','Organizing','Creative']

filename_splitted = line_splited = re.split(r'.json',options.json_file)
print (filename_splitted)
file_offset = filename_splitted[0]

json_handler = JsonHandler()

for i in range(0,int(options.num_content)):
    f = open(options.json_file, 'r')
    csv_handler = CsvHandler(filepath=file_offset+'_'+str(i)+'.csv',header_list=header_list)
    line = f.readline()
    while line:
        line_splited = re.split(r'\t',line.rstrip())
        person_id = line_splited[0]
        json_result = line_splited[1]
        result_dict_list=json_handler.json_user_score_data_to_dict_list(json_result,person_id,i)
        csv_handler.dict_to_csv(dict_list=result_dict_list)
        line = f.readline()
    f.close()
