# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:26:03 2019

@author: laura
"""

import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
iris['class'].value_counts()
x,_,y,_ = train_test_split(iris.iloc[:, 0:4], 
                         iris.iloc[:,4],test_size=0.5,stratify = iris.iloc[:,4])
y.value_counts()

#realizada a mesma divisão estratificada no dataframe "infert"
infert = pd.read_csv('infert.csv')
infert['education'].value_counts()
x1,_,y1,_= train_test_split(infert.iloc[:,2:9], infert.iloc[:,1], 
                         test_size=0.6,stratify = infert.iloc[:,1])