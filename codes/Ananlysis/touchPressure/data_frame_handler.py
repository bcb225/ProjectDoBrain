import pandas as pd
class DataFrameHandler():
    def __init__(self, df_object):
        self.df_object = df_object

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
    def filter_rows_by_is_on_correct_answer(self, status, df_target):
        #return rows filtered by isOnCorrectAnswer status as Pandas DataFrame
        filtered_df = df_target[df_target.isOnCorrectAnswer == status]
        return filtered_df

    def get_mean_touch_pressure(self, df_target):
        #return mean touch pressure of target DataFrame as Numpy matrix

        #get rid of '-1' of touchPressure
        cleaned_df = df_target[df_target.touchPressure != -1]

        #group by person, screenWidth, screenHeight and calculate mean value of touchpressure
        grouped_df = cleaned_df.groupby(['person','screenWidth','screenHeight'])['touchPressure'].mean().reset_index()
        return grouped_df['person'].values, grouped_df['touchPressure'].values