import sys
from csv_loader import CsvLoader
from data_frame_handler import DataFrameHandler
from clustering_analyzer import ClusteringAnalyzer
from main_wrapper import MainWrapper

def parse_commands(argv):
  from optparse import OptionParser
  parser = OptionParser('"')
  parser.add_option('-i', '--inputFile', dest='input_file')
  parser.add_option('-o', '--outputFile', dest='output_file')
  options, otherjunk = parser.parse_args(argv)
  return options

options = parse_commands(sys.argv[1:])

loader = CsvLoader(options.input_file)
loaded_df = loader.load()

handler = DataFrameHandler(loaded_df)

wrapper = MainWrapper(handler)
print(wrapper)
wrapper.proportion_pressure_of_question()
#wrapper.proportion_pressure_of_all()