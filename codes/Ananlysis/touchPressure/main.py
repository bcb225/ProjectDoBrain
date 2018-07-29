import sys
from csv_loader import CsvLoader
from data_frame_handler import DataFrameHandler
from clustering_analyzer import ClusteringAnalyzer

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

sorted_unique_index = handler.get_unique_index()

selected_df_by_index = handler.get_rows_by_index([1,6,1])

true_answer_df = handler.filter_rows_by_correct(selected_df_by_index,True)
false_anwer_df = handler.filter_rows_by_correct(selected_df_by_index,False)

true_mean_pressure_df = handler.get_mean_touch_pressure(true_answer_df)
false_mean_pressure_df = handler.get_mean_touch_pressure(false_anwer_df)

proportion_person_array, proportion_data_array = handler.join_df_and_divide_pressure(true_mean_pressure_df,false_mean_pressure_df,'person')

proportion_pressure_analyzer = ClusteringAnalyzer(proportion_person_array,proportion_data_array)
print(proportion_pressure_analyzer.do_kmeans(2))

#proportion_pressure_analyzer.draw_png(r'$\frac{\text{Mean Wrong Pressure}}{\text{Mean Ture Pressure}}$','test.png')
proportion_pressure_analyzer.draw_png(
    suptitle='',subtitle_1='Kernel Density Estimation',subtitle_2='KMeans Clustering'
    ,xlabel='Mean Wrong Pressure / Mean Correct Pressure',file_path ='test.png'
    )
