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

#Now we will check the distribution of length of the tweets, in terms of words
length_train = train['tweet'].str.len() 
length_test = test['tweet'].str.len() 
plt.hist(length_train, bins=20, label="train_tweets") 
plt.hist(length_test, bins=20, label="test_tweets") 
plt.legend() 
plt.show()

#Data Cleaning
#Combining the datasets will make it convenient for us to pre-process the data
combi = train.append(test, ignore_index=True) 
combi.shape
#remove unwanted text patterns
def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt    

#Removing Twitter Handles (@user)
combi['tidy_tweet'] = np.vectorize(remove_pattern)(combi['tweet'], "@[\w]*") 
combi.head()

#Removing Punctuations, Numbers, and Special Characters

combi['tidy_tweet'] = combi['tidy_tweet'].str.replace("[^a-zA-Z#]", " ") 
combi.head()

#Removing Short Words
combi['tidy_tweet'] = combi['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))

combi.head()

