import pandas as pd
import numpy as np

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from data_frame_handler import  DataFrameHandler
import matplotlib.pyplot as plt
import json

class AssociationAnalyzer:
    def __init__(self, df):
        self.df = df
        
