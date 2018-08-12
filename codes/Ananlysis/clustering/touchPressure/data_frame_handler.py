import pandas as pd
import numpy as np
class DataFrameHandler():
    def __init__(self, df_object):
        self.df_object = df_object
        cleaned_df = df_object[df_object.touchPressure != -1]
        print("shape of df_obj",df_object.shape)
        print("shape of cleaned_df", cleaned_df.shape)
    def get_unique_index(self):
        #return unique index sets of content, question, derivedQuestion as Numpy matrix
        
        #project columns
        all_index = self.df_object[
            ['contentIndex','questionIndex','derivedQuestionIndex']
            ]
        #drop duplicated rows
        unique_index = all_index.drop_duplicates()
        sorted_unique_index = unique_index.sort_values(by=['contentIndex','questionIndex','derivedQuestionIndex'])
        return sorted_unique_index.values
    def get_df_object(self):
        return self.df_object
        
    def get_rows_by_index(self, index_list):
        #return rows selected by index as Pandas DataFrame

        #parse parameter
        contentIndex = index_list[0]
        questionIndex = index_list[1]
        derivedQuestionIndex = index_list[2]

        #selection
        selected_df = self.df_object[
            (self.df_object.contentIndex == contentIndex)
            & (self.df_object.questionIndex == questionIndex) 
            & (self.df_object.derivedQuestionIndex == derivedQuestionIndex) 
            ]
        return selected_df
    def filter_rows_by_correct(self,df_source,status):
        #return rows filtered by isOnCorrectAnswer status as Pandas DataFrame
        filtered_df = df_source[df_source.isOnCorrectAnswer == status]
        return filtered_df

    def get_mean_touch_pressure(self, df_source):
        #return mean touch pressure of target DataFrame as Pandas DataFrame

        #get rid of '-1' of touchPressure
        cleaned_df = df_source[df_source.touchPressure != -1]

        #group by person, screenWidth, screenHeiht and calculate mean value of touchpressure
        grouped_df = cleaned_df.groupby(['person_id','screenWidth','screenHeight'])['touchPressure'].mean().reset_index()
        print("shape",grouped_df.shape)
        return grouped_df

    def join_df_and_divide_pressure(self, df_source_left, df_source_right,key):
        #return joined DataFrame
        df_target = pd.merge(df_source_left,df_source_right,on=key)
        person_array = df_target['person_id'].values
        mean_pressure_true = df_target['touchPressure_x'].values
        mean_pressure_false = df_target['touchPressure_y'].values
        true_false_pressure_proportion = np.divide(mean_pressure_false, mean_pressure_true)
        return person_array, mean_pressure_true, mean_pressure_false, true_false_pressure_proportion
    
