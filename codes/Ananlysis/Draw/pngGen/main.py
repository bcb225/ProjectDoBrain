import sys

from os.path import expanduser
home = expanduser("~")

sys.path.append('{}/ProjectDoBrain/codes/Modules'.format(home))

from csv_loader import CsvLoader
import df_handler
from png_generator import pngGenerator
def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-i', '--dragFile', dest='drag_file')
    parser.add_option('-u', '--userFile', dest='user_file' )

    parser.add_option('-o', '--outputFile', dest='output_file')
    options, otherjunk = parser.parse_args(argv)
    return options


options = parse_commands(sys.argv[1:])

drag_loader = CsvLoader(options.drag_file)
loaded_drag_df = drag_loader.load()

user_loader = CsvLoader(options.user_file)
loaded_user_df = user_loader.load()

sorted_unique_index = df_handler.get_unique_index(loaded_drag_df)

#get first content, game index of drag data
#first_index_list = sorted_unique_index[6]

i = 0
for index_list in sorted_unique_index:
    game_df = df_handler.get_rows_by_index(
        df_source = loaded_drag_df,
        index_list = index_list
    )
    unique_person_and_time_list = df_handler.get_unique_person_and_time(
        df_source = game_df
    )
    
    for person_and_time in unique_person_and_time_list:
        user_level = df_handler.get_user_level_by_person_id(
            df_source = loaded_user_df,
            person_id = person_and_time[0]
        )
        print (user_level)
        print(index_list, person_and_time)
        game_of_the_person = df_handler.get_rows_by_person_and_time(
            df_source = game_df,
            person_and_time = person_and_time
        )
        if len(game_of_the_person) < 3:
            continue
        png_generator = pngGenerator(
            df_object = game_of_the_person,
            index_list = index_list,
            person_and_time = person_and_time,
            user_level = user_level
        )

        png_generator.draw_png()
    