import numpy as np
from scipy import stats

jogadores = [40000,18000,12000,25000,30000,3000,14000,4000,8000]

media = np.mean(jogadores)
print(media)

mediana = np.median(jogadores)
print(mediana)

quartis = np.quantile(jogadores, [0,0.25,0.5,0.75,1])
print(quartis)

#O desvio padrao pode ter resultados diferentes da linguagem R, pois no python o parametro DDOF é N já no R o DDOF é N-1
#Para obter o mesmo resultado que R eu coloco como parametro DDOF =1
desvio_padrao = np.std(jogadores, ddof=1)
print(desvio_padrao)
descricao = stats.describe(jogadores)
print(descricao)