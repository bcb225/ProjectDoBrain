import pandas as pd
import numpy as np
import cv2
import sys
from os import path

from PIL import Image
import scipy
class pngGenerator:
    def __init__(self, df_object):
        self.df_object = df_object
        xy_array_df  = self.df_object[
            ['posX','posY']
        ]
        xy_array_raw = xy_array_df.values
        self.xy_array_int = np.floor(xy_array_raw)
        print(xy_array_raw)

        self.height_and_width_dict = self.get_height_and_width()
    def get_height_and_width(self):
        height_and_width = self.df_object[
            ['screenHeight','screenWidth']
        ]
        #drop duplicated rows
        height_and_width_df = height_and_width.drop_duplicates()
        height_and_width_list = height_and_width.values
        height_and_width_dict ={
            'screenHeight' : height_and_width_list[0][0],
            'screenWidth' : height_and_width_list[0][1]  
        }
        print(height_and_width_dict)
        return height_and_width_dict
    def draw_png(self):
        height = self.height_and_width_dict['screenHeight']
        width = self.height_and_width_dict['screenWidth']
        png_matrix = np.zeros([height, width, 3], dtype=np.uint8)
        png_matrix[:,:] = [255,255,255]

        for i in range(len(self.xy_array_int)-1):
            cv2.line(png_matrix,(int(self.xy_array_int[i][1]),int(self.xy_array_int[i][0])), (int(self.xy_array_int[i+1][1]),int(self.xy_array_int[i+1][0])),(0,0,0),1)
        cv2.imshow('image',png_matrix)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #img = Image.fromarray(png_matrix)
        #img.show()
        pass
