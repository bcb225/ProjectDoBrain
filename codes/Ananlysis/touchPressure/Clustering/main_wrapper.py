from csv_loader import CsvLoader
from clustering_analyzer import ClusteringAnalyzer
import df_handler
class MainWrapper:
    def __init__(self, df_object):
        self.df_object = df_object
    def proportion_pressure_of_question(self):
        sorted_unique_index = df_handler.get_unique_index(self.df_object)
        for index in sorted_unique_index:
            index_list = index.tolist()
            selected_df_by_index = df_handler.get_rows_by_index(self.df_object,index_list)
            true_answer_df = df_handler.filter_rows_by_correct(selected_df_by_index,True)
            false_answer_df = df_handler.filter_rows_by_correct(selected_df_by_index,False)
            
            true_mean_pressure_df = df_handler.group_mean_touch_pressure(true_answer_df)
            false_mean_pressure_df = df_handler.group_mean_touch_pressure(false_answer_df)
            proportion_person_array, mean_pressure_true_array,mean_pressure_false_array,proportion_data_array = df_handler.join_df_and_divide_pressure(true_mean_pressure_df,false_mean_pressure_df,'person_id')
            if len(proportion_person_array) == 0:
                continue
            else:
                png_path = '../../../../files/clustering/pressureProportion/png/'+str(index_list[0])+'_'+str(index_list[1])+'_'+str(index_list[2])+'.png'
                csv_path = '../../../../files/clustering/pressureProportion/csv/'+str(index_list[0])+'_'+str(index_list[1])+'_'+str(index_list[2])+'.csv'
                print(
                    'Clustering data from contentIndex[%d]:questionIndex[%d]:derivedQuestionIndex[%d]\t%d users'
                    %(index_list[0],index_list[1],index_list[2],len(proportion_person_array) ))
                proportion_pressure_analyzer = ClusteringAnalyzer(proportion_person_array, mean_pressure_true_array,mean_pressure_false_array,proportion_data_array)
                proportion_pressure_analyzer.do_kmeans(n_clusters=2)
                proportion_pressure_analyzer.draw_png(
                    suptitle='',subtitle_1='Kernel Density Estimation',subtitle_2='KMeans Clustering'
                    ,xlabel='Mean Wrong Pressure / Mean Correct Pressure',file_path =png_path
                    )
                proportion_pressure_analyzer.write_result_for_proportion(file_path=csv_path)
        return 
    def proportion_pressure_of_all(self):
        true_answer_df = df_handler.filter_rows_by_correct(self.df_object,True)
        false_answer_df = df_handler.filter_rows_by_correct(self.df_object,False)
        true_mean_pressure_df = df_handler.group_mean_touch_pressure(true_answer_df)
        false_mean_pressure_df = df_handler.group_mean_touch_pressure(false_answer_df)
        
        proportion_person_array, mean_pressure_true_array,mean_pressure_false_array,proportion_data_array = df_handler.join_df_and_divide_pressure(true_mean_pressure_df,false_mean_pressure_df,'person_id')
        if len(proportion_person_array) == 0:
            pass
        else:
            png_path = '../../../../files/clustering/pressureProportion/png/total_result.png'
            csv_path = '../../../../files/clustering/pressureProportion/csv/total_result.csv'
            proportion_pressure_analyzer = ClusteringAnalyzer(proportion_person_array, mean_pressure_true_array,mean_pressure_false_array,proportion_data_array)
            proportion_pressure_analyzer.do_kmeans(n_clusters=2)
            proportion_pressure_analyzer.draw_png(
                suptitle='',subtitle_1='Kernel Density Estimation',subtitle_2='KMeans Clustering'
                ,xlabel='Mean Wrong Pressure / Mean Correct Pressure',file_path =png_path)
            proportion_pressure_analyzer.write_result_for_proportion(file_path=csv_path)
        return
