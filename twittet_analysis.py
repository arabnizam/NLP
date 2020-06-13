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

#%matplotlib inline

import os
os.listdir()
os.chdir("D:\\git_NLP\\NLP")
os.listdir()

train  = pd.read_csv('train_Twitter Analysis.csv') 
train
test = pd.read_csv('test_Twitter Analysis.csv')
test
#Data Inspection
#Let’s check out a few non racist/sexist tweets.
train.head()

train[train['label'] == 0].head()
#Now check out a few racist/sexist tweets.
train[train['label'] == 1].head(10)

#Let’s check dimensions of the train and test dataset.
train.shape, test.shape
#((31962, 3), (17197, 2))

#check the distribution
train['label'].value_counts()

train['tweet'].str.len()




