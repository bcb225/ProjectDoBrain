import pandas as pd
import numpy as np

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from data_frame_handler import  DataFrameHandler
from scipy import stats
import matplotlib.pyplot as plt
import json

class AssociationAnalyzer:
    def __init__(self, df_object):
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
        
    def t_test(self):
        for level_1 in self.level_list:
            for level_2 in self.level_list:
                statistic, pvalue = stats.ttest_ind(self.touchPressure_dict[level_1],self.touchPressure_dict[level_2])
                print(statistic,pvalue)
                
    def draw_box_plot(self):
        np_list = []
        
        for level in self.level_list:
            np_list.append(self.touchPressure_dict[level])

        xtick_list =[]

        xtick_list.append('A')
        xtick_list.append('B')
        xtick_list.append('C')

        fig, ax1 = plt.subplots()
        
        bp = ax1.boxplot(np_list, 0 ,'')
        ax1.set_xticklabels(xtick_list)
        plt.show()
