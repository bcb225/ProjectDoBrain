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

for index in sorted_unique_index:
    index_list = index.tolist()
    selected_df_by_index = handler.get_rows_by_index(index_list)
    true_answer_df = handler.filter_rows_by_correct(selected_df_by_index,True)
    false_answer_df = handler.filter_rows_by_correct(selected_df_by_index,False)
    
    true_mean_pressure_df = handler.get_mean_touch_pressure(true_answer_df)
    false_mean_pressure_df = handler.get_mean_touch_pressure(false_answer_df)
    
    proportion_person_array, proportion_data_array = handler.join_df_and_divide_pressure(true_mean_pressure_df,false_mean_pressure_df,'person')
    
    if len(proportion_person_array) == 0:
        continue
    else:
        png_path = '../../../files/clustering/pressureProportion/png/'+str(index_list[0])+'_'+str(index_list[1])+'_'+str(index_list[2])+'.png'
        csv_path = '../../../files/clustering/pressureProportion/csv/'+str(index_list[0])+'_'+str(index_list[1])+'_'+str(index_list[2])+'.csv'
        print(
            'Clustering data from contentIndex[%d]:questionIndex[%d]:derivedQuestionIndex[%d]\t%d users'
            %(index_list[0],index_list[1],index_list[2],len(proportion_person_array) )
            )
        proportion_pressure_analyzer = ClusteringAnalyzer(proportion_person_array,proportion_data_array)
        proportion_pressure_analyzer.do_kmeans(n_clusters=2)
        proportion_pressure_analyzer.draw_png(
            suptitle='',subtitle_1='Kernel Density Estimation',subtitle_2='KMeans Clustering'
            ,xlabel='Mean Wrong Pressure / Mean Correct Pressure',file_path =png_path
            )
        proportion_pressure_analyzer.write_result(file_path=csv_path)
