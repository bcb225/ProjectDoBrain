import sys
from firebase_connector import FirebaseConnector
import requests

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

base_url = 'https://dobrain-pro.firebaseio.com/drag_data/iOS/'

for person in person_list:
    target_url = base_url + person +'.json?print=pretty'
    resp = requests.get(url=target_url)
    json_text = resp.json()
    print(json_text)
"""connector = FirebaseConnector(options.key_file)

data = connector.get_drag_data_by_person_id('000123DB-6507-424D-86A2-770DB247D396')

access_token = connector.get_access_token()

data_via = connector.get_drag_data_by_person_id_with_access_token('000123DB-6507-424D-86A2-770DB247D396')

print(data)
print(access_token)
print(data_via)"""