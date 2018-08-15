import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from csv_loader import CsvLoader
from data_frame_handler import  DataFrameHandler
from association_analyzer import AssociationAnalyzer
def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-d', '--dragFile', dest='drag_file')
    parser.add_option('-u', '--userFile', dest='user_file' )
    parser.add_option('-o', '--outputFile', dest='output_file')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

drag_loader = CsvLoader(options.drag_file)
loaded_drag_df = drag_loader.load()

user_loader = CsvLoader(options.user_file)
loaded_user_df = user_loader.load()

user_handler = DataFrameHandler(loaded_user_df)
drag_handler = DataFrameHandler(loaded_drag_df)

#clean drag_handler df object (remove -1 touchPressure)
drag_handler.remove_minus_pressure()

#get sorted unique index of drag data
sorted_unique_index = drag_handler.get_unique_index()

#get first content, game index of drag data
first_index_list = sorted_unique_index[0]

selected_drag_df_by_index = drag_handler.get_rows_by_index(first_index_list)

joined_df_by_person_id = drag_handler.join_df_by_key(loaded_user_df,selected_drag_df_by_index,'person_id')

association_analyzer = AssociationAnalyzer(joined_df_by_person_id)

print(joined_df_by_person_id)