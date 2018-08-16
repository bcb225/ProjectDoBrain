import pandas as pd
import numpy as np

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from scipy import stats
from itertools import combinations

from csv_handler import CsvHandler
import matplotlib.pyplot as plt
import json

class AssociationAnalyzer:
    def __init__(self, df_object, index_list, file_path):
        self.df_object = df_object
        self.df_dict = {
            'A' : df_object.loc[df_object['level'] == 'A'],
            'B' : df_object.loc[df_object['level'] == 'B'],
            'C' : df_object.loc[df_object['level'] == 'C']
        }
        self.touchPressure_dict = {
            'A' : self.df_dict['A']['touchPressure'].values,
            'B' : self.df_dict['B']['touchPressure'].values,
            'C' : self.df_dict['C']['touchPressure'].values
        }
        self.level_list = ['A', 'B', 'C']
        
        self.level_info_dict_list = []
        for level in self.level_list:
            level_info_dict = {
                'group' : level,
                'count' : self.df_dict[level].shape[0]
            }
            self.level_info_dict_list.append(level_info_dict)
        print(self.level_info_dict_list)
        self.index_str = str(index_list[0]) + '_' + str(index_list[1]) + '_' +str(index_list[2])

        self.png_path = file_path + '/png/' + self.index_str + '.png'
        self.csv_ttest_path = file_path + '/csv/ttest/' + self.index_str + '.csv'
        self.csv_info_path = file_path + '/csv/info/' + self.index_str + '.csv'

        self.t_stat_header_list = ['group 1', 'group 2', 't-statistic', 'p-value']
        self.level_info_header_list = ['group', 'count']
    def t_test(self):
        self.statistic_dict_list = []
        for combo in combinations(self.level_list,2):
            
            combo_list = list(combo)
            statistic, pvalue = stats.ttest_ind(
                self.touchPressure_dict[combo_list[0]],
                self.touchPressure_dict[combo_list[1]]
                )
            temp_statistic_dict = {
                'group 1' : combo_list[0],
                'group 2' : combo_list[1],
                't-statistic' : statistic,
                'p-value' : pvalue
                }
            self.statistic_dict_list.append(temp_statistic_dict)

        return self.statistic_dict_list
                
    def draw_box_plot(self):
        print(self.statistic_dict_list)
        
        np_list = []
        xtick_list = []
        for level in self.level_list:
            np_list.append(self.touchPressure_dict[level])
            xtick_list.append(level)
            y = self.touchPressure_dict[level].max()

        fig, ax = plt.subplots()
        
        bp = ax.boxplot(np_list, 1 ,'')
        ax.set_xticklabels(xtick_list)
        ax.set_xlabel('Group')
        ax.set_ylabel('Mean Touch Pressure')
        ax.set_title(self.index_str)
        group_A = 0
        group_B = 1
        group_C = 2

        plt.savefig(self.png_path)

        plt.clf()
    
    def save_statistics_as_csv(self):
        statistic_csv_handler = CsvHandler(
            filepath = self.csv_ttest_path,
            header_list = self.t_stat_header_list
        )
        statistic_csv_handler.dict_to_csv(
            dict_list = self.statistic_dict_list
        )

    def save_record_info_as_csv(self):
        info_csv_handler = CsvHandler(
            filepath = self.csv_info_path,
            header_list = self.level_info_header_list
        )
        info_csv_handler.dict_to_csv(
            dict_list = self.level_info_dict_list
        )