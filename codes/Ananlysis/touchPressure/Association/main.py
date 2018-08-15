import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from csv_loader import CsvLoader
from association_analyzer import AssociationAnalyzer
import df_handler
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

#clean drag_handler df object (remove -1.0000 touchPressure)
minus_one_removed_df = df_handler.remove_minus_pressure(loaded_drag_df)

#clean drag_handler df object (remove 1.0000 touchPressure of drag_handler's df_object)
plus_one_removed_df = df_handler.remove_one_pressure(minus_one_removed_df)

# get sorted unique index of drag data
sorted_unique_index = df_handler.get_unique_index(plus_one_removed_df)

#get first content, game index of drag data
first_index_list = sorted_unique_index[0]

#select first game as interest
selected_drag_df_by_index = df_handler.get_rows_by_index(plus_one_removed_df,first_index_list)

#group by personId and get mean touch pressure of the game
group_mean_touch_pressure_df = df_handler.group_mean_touch_pressure(selected_drag_df_by_index)

#clean mean touch pressure (grouped) as df_source (remove 1.0000 mean touchPressure of df_source)
#NOT drag_handler's df_object
plus_one_removed_grouped_df = df_handler.remove_one_pressure(group_mean_touch_pressure_df)

#join user level table and drag data table with key person_id
joined_by_person_id_df = df_handler.join_df_by_key(loaded_user_df,plus_one_removed_grouped_df,'person_id')

#create AssociationAnalyzer module
association_analyzer = AssociationAnalyzer(joined_by_person_id_df)

#t_test
association_analyzer.t_test()

#draw box plot
association_analyzer.draw_box_plot()