import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from data_frame_handler import  DataFrameHandler
from csv_loader import CsvLoader
from box_plot_analyzer import BoxPlotAnalyzer
def parse_commands(argv):
    from optparse import OptionParser
    parser = OptionParser('"')
    parser.add_option('-d', '--dragFile', dest='drag_file')
    parser.add_option('-o', '--outputFile', dest='output_file')
    options, otherjunk = parser.parse_args(argv)
    return options

options = parse_commands(sys.argv[1:])

drag_loader = CsvLoader(options.drag_file)
loaded_drag_df = drag_loader.load()

drag_handler = DataFrameHandler(loaded_drag_df)

#get screen size (x,y) set
screen_size_dict_list = drag_handler.get_screen_size_set()

drag_handler.remove_minus_pressure()

print (screen_size_dict_list)
box_plot_analyzer = BoxPlotAnalyzer(df_handler = drag_handler)

box_plot_analyzer.draw_box_plot()
