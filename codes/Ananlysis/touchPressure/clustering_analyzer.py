import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
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

    def do_kmeans(self):
        X = np.array(self.data_matrix_2d)
        kmeans = KMeans(n_clusters=2,random_state=0).fit(X)
        return kmeans.labels_

    def draw_png(self):
        pass
