import pandas as pd
import numpy as np

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from scipy import stats
from itertools import combinations

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
        self.statistic_dict_list = []
        self.pvalue_dict_list = []
        for combo in combinations(self.level_list,2):
            
            combo_list = list(combo)
            statistic, pvalue = stats.ttest_ind(
                self.touchPressure_dict[combo_list[0]],
                self.touchPressure_dict[combo_list[1]]
                )
            temp_statistic_dict = {
                combo_list[0] : {
                    combo_list[1] : statistic
                }
            }
            temp_pvalue_dict = {
                combo_list[0] : {
                    combo_list[1] : pvalue
                }
            }
            self.statistic_dict_list.append(temp_statistic_dict)
            self.pvalue_dict_list.append(temp_pvalue_dict)
        
                
    def draw_box_plot(self):
        print(self.statistic_dict_list)
        print(self.pvalue_dict_list)
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
        ax.set_title('Box Plot of First Content')
        group_A = 0
        group_B = 1
        group_C = 2
        ax.text(
            x=(group_A+group_B)*0.5,
            y=y+2,
            s='ss'
            )
        plt.show()
