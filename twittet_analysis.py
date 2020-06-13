import re    # for regular expressions 
import nltk  # for text manipulation 
import string 
import warnings 
import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt  

pd.set_option("display.max_colwidth", 200) 
warnings.filterwarnings("ignore", category=DeprecationWarning) 

%matplotlib inline

train  = pd.read_csv('train_Twitter Analysis.csv') 
train
test = pd.read_csv('test_Twitter Analysis.csv')
test
import os
os.listdir()