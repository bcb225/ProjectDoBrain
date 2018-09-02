import sys
from os.path import expanduser
home = expanduser("~")

sys.path.append('{}/ProjectDoBrain/codes/Modules'.format(home))

from csv_loader import CsvLoader
import df_handler
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

minus_pressure_removed_df = df_handler.remove_minus_pressure(loaded_drag_df)

box_plot_analyzer = BoxPlotAnalyzer(minus_pressure_removed_df)

box_plot_analyzer.draw_box_plot()
