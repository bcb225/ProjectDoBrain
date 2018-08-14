import pandas as pd
import numpy as np

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from data_frame_handler import  DataFrameHandler
import matplotlib.pyplot as plt
import json

class BoxPlotAnalyzer:
    def __init__(self, df_handler):
        self.df_handler = df_handler
        self.screen_size_dict_list = self.df_handler.get_screen_size_set()
        print(self.screen_size_dict_list)
    def draw_box_plot(self):
        np_list = []
        for screen_size_dict in self.screen_size_dict_list:
            selected_df_by_screen_size = self.df_handler.get_rows_by_screen_size(screen_size_dict)
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