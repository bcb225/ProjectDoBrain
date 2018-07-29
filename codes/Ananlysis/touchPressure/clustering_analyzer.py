import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import rc
import matplotlib.pyplot as plt
import csv

class ClusteringAnalyzer:
    def __init__(self, label_array, data_array):
        self.label_array = label_array
        self.data_array_1d = data_array
        
        #make an array filled with zeros
        zero_arr = np.zeros(len(self.data_array_1d))
        #append the zero array to existing 1-dimensional data input
        appended_arr = np.append(self.data_array_1d,zero_arr)
        #reshape to 2-dimensional data matrix
        reshaped_arr = appended_arr.reshape(2,len(self.data_array_1d))
        #transpose the matrix to get (x,y) coordinates
        self.data_matrix_2d = reshaped_arr.T

    def do_kmeans(self,n_clusters):
        self.X = np.array(self.data_matrix_2d)
        self.kmeans = KMeans(n_clusters=n_clusters,random_state=0).fit(self.X)
        return self.kmeans.labels_

    def draw_png(self,suptitle,subtitle_1,subtitle_2,xlabel,file_path):
        #rc('text',usetex = True)
        #rc('font',family = 'serif')

        #Kernel Density Estimation
        data_ser = pd.Series(self.data_array_1d)    #set Series
        ax1 = plt.subplot(211)  #ready first subplot (ax1 is axis)
        plt.title(subtitle_1)   #set subtitle
        plt.xlabel(xlabel)      #set xlabel
        data_ser.plot.kde()     #calculate kernal density estimation
        
        #Clustering Scatter
        plt.subplot(212,sharex = ax1)   #reday second subplot with shared axis-X
        plt.title(subtitle_2)           #set subtitle
        plt.scatter(self.X[:,0],self.X[:,1],c=self.kmeans.labels_)  #scatter clustering result
        plt.xlabel(xlabel)              #set xlabel
        plt.yticks([])                  #remove yticks

        plt.subplots_adjust(hspace = 0.8)   #adjust vertical white space

        plt.suptitle(suptitle)  #set superior title
        plt.savefig(file_path)  #save figure as file_path
    
    def write_result(self,file_path):
        group_0 = self.label_array[self.kmeans.labels_ == 0]
        group_1 = self.label_array[self.kmeans.labels_ == 1]
        print(self.label_array, self.kmeans.labels_)
        print(self.kmeans.labels_ == 0)
        print(group_0, group_1)
        print(len(self.label_array),len(group_0), len(group_1))

        #make an array filled with zeros
        zero_arr = np.zeros(len(group_0))
        #append the zero array to existing 1-dimensional data input
        zero_appended_arr = np.append(group_0,zero_arr)
        #reshape to 2-dimensional data matrix
        zero_reshaped_arr = zero_appended_arr.reshape(2,len(group_0))
        #transpose the matrix to get (x,y) coordinates
        zero_transpose_arr = zero_reshaped_arr.T

        #make an array filled with zeros
        one_arr = np.ones(len(group_1))
        #append the zero array to existing 1-dimensional data input
        one_appended_arr = np.append(group_1,one_arr)
        #reshape to 2-dimensional data matrix
        one_reshaped_arr = one_appended_arr.reshape(2,len(group_1))
        #transpose the matrix to get (x,y) coordinates
        one_transpose_arr = one_reshaped_arr.T

        result_arr = np.vstack([zero_transpose_arr,one_transpose_arr])
        np.savetxt(
            fname=file_path
            ,X=result_arr,delimiter=','
            ,fmt='%s'
            ,header='personId,groupId'
            ,comments=''
            )