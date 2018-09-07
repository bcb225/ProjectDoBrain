import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rest_handler import RestHandler
from json_handler import JsonHandler
from csv_handler import CsvHandler

def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-p', '--personFile', dest='person_file')
    parser.add_option('-m', '--mobileOs', dest='mobile_os')

    options, otherjunk = parser.parse_args(argv)
    return options

#make person_id csv without HEADER

options = parse_commands(sys.argv[1:])

header_list = ["person_id"]

rest_handler = RestHandler(mobile_os=options.mobile_os)
json_handler = JsonHandler()
csv_handler = CsvHandler(filepath=options.person_file,header_list=header_list)

json_result = rest_handler.get_json_of_person_id()
result_dict_list = json_handler.json_person_id_to_dict_list(json_source = json_result, mobile_os=options.mobile_os)
csv_handler.dict_to_csv(dict_list=result_dict_list)