import pandas as pd
import numpy as np
import cv2
import sys

import os
from os import path
from os.path import expanduser


from PIL import Image
import scipy
class pngGenerator:
    def __init__(self, df_object, index_list, person_and_time,user_level):
        self.df_object = df_object
        self.user_level = user_level
        self.get_questionManagerCategory()
        #get height and width info as dict type
        self.height_and_width_dict = self.get_height_and_width()
        self.height = self.height_and_width_dict['screenHeight']
        self.width = self.height_and_width_dict['screenWidth']
        
        #make png file path
        self.png_path = self.make_path(
            index_list = index_list,
            person_and_time = person_and_time
        )
        
        xy_array_df  = self.df_object[
            ['posX','posY']
        ]
        xy_array_raw = xy_array_df.values

        #convert x,y coordinate to pixel (floor)
        self.xy_array_int = np.floor(xy_array_raw)
        #print(xy_array_raw)


    def get_height_and_width(self):
        #return height and width info as dict type
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
    def get_questionManagerCategory(self):
        questionManagerCategory = self.df_object[
            ['questionManagerCategory']
        ]
        questionManagerCategory_df = questionManagerCategory.drop_duplicates()
        questionManagerCategory_list = questionManagerCategory.values

        self.questionManagerCategory_txt = questionManagerCategory_list[0][0]
        
    def draw_png(self):

        
        png_matrix = np.zeros([self.height, self.width, 3], dtype=np.uint8)
        png_matrix[:,:] = [255,255,255]

        #connect to sequential dots
        for i in range(len(self.xy_array_int)-1):
            first_dot_x = int(self.xy_array_int[i][1])
            first_dot_y = int(self.xy_array_int[i][0])

            second_dot_x = int(self.xy_array_int[i+1][1])
            second_dot_y = int(self.xy_array_int[i+1][0])
            cv2.line(png_matrix,(first_dot_x,first_dot_y), (second_dot_x,second_dot_y),(0,0,0),1)
        
        status = cv2.imwrite(self.png_path,png_matrix)
        #status = cv2.imwrite('local.png',png_matrix)
        print(status    )
        #cv2.waitKey(0)
        cv2.destroyAllWindows()

    def make_path(self, index_list, person_and_time):
        home = expanduser("~")
        file_path = '{}/ProjectDoBrain/results/Draw/{}/{}_{}_{}/{}X{}/{}/'.format(
            home,
            self.questionManagerCategory_txt,
            index_list[0],
            index_list[1],
            index_list[2],
            self.height,
            self.width,
            self.user_level
        )
        result_path = '{}/{}.png'.format(
            file_path,
            person_and_time[0] #this is person_id
        )

        if not os.path.exists(file_path):
            print('created')
            os.makedirs(file_path)

        print(result_path)
        return result_path
