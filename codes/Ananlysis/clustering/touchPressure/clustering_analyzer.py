import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import rc
import matplotlib.pyplot as plt
import csv

class ClusteringAnalyzer:
    def __init__(self, label_array, mean_true_pressure_array,mean_false_pressure_array ,data_array):
        
        self.label_array = label_array[~(np.isnan(data_array)|np.isinf(data_array))]
        self.data_array_1d = data_array[~(np.isnan(data_array)|np.isinf(data_array))]
        
        self.mean_true_pressure_array = mean_true_pressure_array[~(np.isnan(data_array)|np.isinf(data_array))]
        self.mean_false_pressure_array = mean_false_pressure_array[~(np.isnan(data_array)|np.isinf(data_array))]
        outlier_1 = self.is_out_lier_z(self.data_array_1d)
        print(outlier_1)
        outlier_2 = self.is_out_lier(self.data_array_1d)
        print(outlier_2)	
        #make an array filled with zeros
        zero_arr = np.zeros(len(self.data_array_1d))
        #append the zero array to existing 1-dimensional data input
        appended_arr = np.append(self.data_array_1d,zero_arr)
        #reshape to 2-dimensional data matrix
        reshaped_arr = appended_arr.reshape(2,len(self.data_array_1d))
        #transpose the matrix to get (x,y) coordinates
        self.data_matrix_2d = reshaped_arr.T
        
    def is_out_lier_z (self,data_array):
        threshold = 3
        
        mean = np.mean(data_array)
        stdev = np.std(data_array)
        z_scores = [(y - mean) / stdev for y in data_array]
        
        return np.where(np.abs(z_scores) > threshold)
        
    def is_out_lier(self, data_array):
        threshold = 3.5
        median = np.median(data_array)
        median_absolute_deviation = np.median([np.abs(y-median) for y in data_array	])
        modified_z_scores = [0.6745 * (y - median) / median_absolute_deviation for y in data_array]
        return (np.where(np.abs(modified_z_scores) > threshold))
    def do_kmeans(self,n_clusters):
        self.X = np.array(self.data_matrix_2d)
        if len(self.X) < 2:
            self.kmeans = KMeans(n_clusters=1,random_state=0).fit(self.X)
        else:
            self.kmeans = KMeans(n_clusters=n_clusters,random_state=0).fit(self.X)
        return self.kmeans.labels_

    def draw_png(self,suptitle,subtitle_1,subtitle_2,xlabel,file_path):
        #rc('text',usetex = True)
        #rc('font',family = 'serif')
        if len(self.data_array_1d) == 1:
            return
        
        #Kernel Density Estimation
        data_ser = pd.Series(self.data_array_1d)    #set Series
        ax1 = plt.subplot(211)  #ready first subplot (ax1 is axis)
        plt.title(subtitle_1)   #set subtitle
        plt.xlabel(xlabel)      #set xlabel
        data_ser.plot.kde()     #calculate kernal density estimation
        
        #Clustering Scatter
        self.check_and_swap()
        plt.subplot(212,sharex = ax1)   #reday second subplot with shared axis-X
        plt.title(subtitle_2)           #set subtitle
        plt.scatter(self.X[:,0],self.X[:,1],c=self.kmeans.labels_)  #scatter clustering result
        plt.xlabel(xlabel)              #set xlabel
        plt.yticks([])                  #remove yticks

        plt.subplots_adjust(hspace = 0.8)   #adjust vertical white space

        plt.suptitle(suptitle)  #set superior title
        plt.savefig(file_path)  #save figure as file_path
    
        plt.clf()

	def write_result_for_true(self,file_path):
		if len(self.data_array_1d) == 1:
			return 
		
		pass
	
	def write_result_for_false(self,file_path):
		pass

    def write_result_for_proportion(self,file_path):
        if len(self.data_array_1d) == 1:
            return
        group_0 = self.label_array[self.kmeans.labels_ == 0]
        group_1 = self.label_array[self.kmeans.labels_ == 1]
        group_0_false = self.mean_false_pressure_array[self.kmeans.labels_ == 0]
        group_1_false = self.mean_false_pressure_array[self.kmeans.labels_ == 1]
        group_0_true = self.mean_true_pressure_array[self.kmeans.labels_ == 0]
        group_1_true = self.mean_true_pressure_array[self.kmeans.labels_ == 1]
        group_0_proportion = self.data_array_1d[self.kmeans.labels_ == 0]
        group_1_proportion = self.data_array_1d[self.kmeans.labels_ == 1]
        #make an array filled with zeros
        zero_arr = np.zeros(len(group_0))
        #append the zero array to existing 1-dimensional data input
        zero_appended_arr = np.append(group_0,zero_arr)
        zero_appended_false_pressure = np.append(zero_appended_arr,group_0_false)
        zero_appended_true_pressure = np.append(zero_appended_false_pressure,group_0_true)
        zero_appended_proportion_pressure = np.append(zero_appended_true_pressure,group_0_proportion)
        #reshape to 2-dimensional data matrix
        zero_reshaped_arr = zero_appended_proportion_pressure.reshape(5,len(group_0))
        #transpose the matrix to get csv format
        zero_transpose_arr = zero_reshaped_arr.T

        #make an array filled with ones
        one_arr = np.ones(len(group_1))
        #append the one array to existing 1-dimensional data input
        one_appended_arr = np.append(group_1,one_arr)
        one_appended_false_pressure = np.append(one_appended_arr,group_1_false)
        one_appended_true_pressure = np.append(one_appended_false_pressure,group_1_true)
        one_appended_proportion_pressure = np.append(one_appended_true_pressure,group_1_proportion)
        #reshape to 2-dimensional data matrix
        one_reshaped_arr = one_appended_proportion_pressure.reshape(5,len(group_1))
        #transpose the matrix to get csv format
        one_transpose_arr = one_reshaped_arr.T

        result_arr = np.vstack([zero_transpose_arr,one_transpose_arr])
        np.savetxt(
            fname=file_path
            ,X=result_arr,delimiter=','
            ,fmt='%s'
            ,header='personId,groupId,falsePressure,truePressure,ProportionPressure'
            ,comments=''
            )
    
    def check_and_swap(self):
        group_0 = self.data_array_1d[self.kmeans.labels_ == 0]
        group_1 = self.data_array_1d[self.kmeans.labels_ == 1]

        #check whether group 0(contrl) has large pressure proportion than group 1(case)
        if np.amin(group_0) >= np.amax(group_1):    #if so, do swap
            self.do_swap()

    def do_swap(self):
        temp_labels = self.kmeans.labels_.copy()    #shallow copy of kmeans.labels_
        self.kmeans.labels_[temp_labels == 0] = 1   #do swap
        self.kmeans.labels_[temp_labels == 1] = 0
        return