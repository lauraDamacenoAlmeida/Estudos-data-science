# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:47:52 2019

@author: laura
"""
import numpy as np
import pandas as pd

base = pd.read_csv('iris.csv')
base
#informações dos numeros de linhas,colunas
base.shape
#utilizado quando eu quero que a amostra seja a mesma
np.random.seed(12)

amostra = np.random.choice(a = [0,1],size = 150,replace = True, p = [0.5,0.5])
len(amostra)
len(amostra[amostra==1])
len(amostra[amostra==0])