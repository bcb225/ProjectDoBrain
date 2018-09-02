import sys

from os.path import expanduser
home = expanduser("~")

sys.path.append('{}/ProjectDoBrain/codes/Modules'.format(home))

from csv_loader import CsvLoader
import df_handler
def parse_commands(argv):
  from optparse import OptionParser
  parser = OptionParser('"')
  parser.add_option('-i', '--dragFile', dest='drag_file')
  parser.add_option('-o', '--outputFile', dest='output_file')
  options, otherjunk = parser.parse_args(argv)
  return options


options = parse_commands(sys.argv[1:])

drag_loader = CsvLoader(options.drag_file)
loaded_drag_df = drag_loader.load()

first_game_df = df_handler.get_rows_by_index(
    df_source = loaded_drag_df,
    index_list = [1,6,0]
)

unique_person_and_time_list = df_handler.get_unique_person_and_time(
    df_source = first_game_df
)
print(first_game_df)
print(unique_person_and_time_list)