import sys
from os.path import expanduser
home = expanduser("~")
sys.path.append('{}/ProjectDoBrain/codes/Modules'.format(home))

from csv_loader import CsvLoader
from clustering_analyzer import ClusteringAnalyzer
from main_wrapper import MainWrapper

def parse_commands(argv):
  from optparse import OptionParser
  parser = OptionParser('"')
  parser.add_option('-i', '--dragFile', dest='drag_file')
  parser.add_option('-o', '--outputFile', dest='output_file')
  options, otherjunk = parser.parse_args(argv)
  return options

options = parse_commands(sys.argv[1:])

loader = CsvLoader(options.drag_file)
loaded_df = loader.load()

wrapper = MainWrapper(loaded_df)
print(wrapper)
wrapper.proportion_pressure_of_question()
#wrapper.proportion_pressure_of_all()