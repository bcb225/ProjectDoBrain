import pandas as pd
import numpy as np

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import matplotlib.pyplot as plt
import json
import df_handler

class BoxPlotAnalyzer:
    def __init__(self, df_object):
        self.df_object = df_object
        self.screen_size_dict_list = df_handler.get_screen_size_set(self.df_object)
        print(self.screen_size_dict_list)
    def draw_box_plot(self):
        np_list = []
        for screen_size_dict in self.screen_size_dict_list:
            selected_df_by_screen_size = df_handler.get_rows_by_screen_size(self.df_object,screen_size_dict)
            touchPressure_array = selected_df_by_screen_size['touchPressure'].values
            np_list.append(touchPressure_array)
        fig, ax1 = plt.subplots()
        xtick_list =[]
        for screen_size_set in self.screen_size_dict_list:
            x_tick = str(screen_size_set['screenWidth']) + " X " + str(screen_size_set['screenHeight'])
            xtick_list.append(x_tick)
        bp = ax1.boxplot(np_list, 0 ,'')
        ax1.set_xticklabels(xtick_list, rotation=45)
        plt.show()