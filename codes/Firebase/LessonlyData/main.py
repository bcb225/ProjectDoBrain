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
    parser.add_option('-l', '--lessonFile', dest='lesson_file')
    parser.add_option('-p', '--personFile', dest='person_file')
    parser.add_option('-m', '--mobileOS', dest='mobile_os')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

header_list = [
    'index','person_id', 'level',
    'attentionMemory','constructionalAbility',
    'discernment','logicalReasoning','mathematicalThinking',
    'reaction','spatialPerception'
    ]

rest_handler = RestHandler(mobile_os=options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.lesson_file,header_list=header_list)
for index in range(0,60):
    print( index)
    json_result = rest_handler.get_lesson_bucket_data_by_index(index = index)
    if not json_result is None:
        result_dict_list = json_handler.json_lesson_bucket_data_to_dict_list(json_result,index)
        csv_handler.dict_to_csv(dict_list = result_dict_list)