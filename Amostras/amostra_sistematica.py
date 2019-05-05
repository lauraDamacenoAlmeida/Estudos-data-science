# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:05:59 2019

@author: laura
"""

import numpy as np
import pandas as pd
from math import ceil

#temos uma populaçãi de 150 elementos e eu quero selecionar 15 elementos
populacao = 150
amostra = 15
#utilizamos o ceil para fazer o arredondamento para cima da divisão
k = ceil(populacao/amostra)

#preciso fazer um sortei de um numero que esteja dentro deste intervalo de K
#.randint() ==> gera um numero aleatorio, 1 parametro define o limite inferior, 2 parametro é limite superior

r = np.random.randint(low = 1, high = k+1, size = 1)
#vai armazenar o valor de R
acumulador = r[0]

sorteados = []
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k
    
base = pd.read_csv('iris.csv')
#pegar os elementos selecionados, .loc ==> faz a localização dos elementos
base_final = base.loc[sorteados]