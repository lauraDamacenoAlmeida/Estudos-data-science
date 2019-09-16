#import pandas as pd
#Se eu quero carregar um arq CSV uso a funcao: csv_path = 'file.csv'
#df = pd.read_csv(csv_path) ==> retorna um dataframe
#Um jeito de trabalhar com dados no pandas é usando data frame
#df.head() ==> imprimimos as 5 primeiras linhas no dataframe
#ler excel xlsx_path = 'file.xlsx'
#df = pd.read_excel(xlsx_path)
#df.head()
#um dataframe é composto por linha e colunas. Podemos criar dataframes a partir de um dicionário, onde as chaves serão as colunas e os valores as linhas.\
#ex: songs{'album':[thriller,Back in black],'released':[1982,1980]}
#para converter em dataframe ==> songs_frame = pd.DataFrame(songs)
#podemos criar dataframes com 1 coluna x = [['coluna1']]
#pegar valores: df.ix[0,0] ==> imprimir o valor linha X posLinha ==> para pegar valor linha X coluna [0,'album'] acessar valor da linha 0 na coluna ALbum
# de uma coluna até outra coluna z = df.ix[0:2, 'Artist':'Released']

#Posso filtrar os valores aparecidos, onde através do meu filtro é gerado uma tabela de valores booleanos. ex: df['Released']>=1980
#Podemos selecionar as colunas especificadas em uma linha; nós simplesmente usamos os nomes do dataframe,
# e entre colchetes colocamos a desigualdade mencionada anteriormente e a atribuímos aovariável df1. Ex: df1=df[df['Released']>=1980]
#Para salvar esse novo dataframe em um modelo CSV usamos a seguinte sintaxe df1.to_csv('novoArquivo.csv') ==> onde passamo como arguento o nome do novo arq

#NUMPY
#1D ARRAY ==> Numpy array ou ndarray é similar a uma lista. Tem um tamanho fixo e cada elemento dentro dela tem o mesmo tipo.
# Para usar: import numpy as np
# a  = np.array([0,1,2,3,4])
#Os valores podem ser acessados pelo seus índies a[0]. type(a) ==> valor = numpy.ndarray
#Pegar o tipo dos dados armazenados: a.dtype Pegar tam da array a.size

# a.ndim Number of array dimensions..

#Tupla de dimensões de matriz.: a.shape
#Como em listas e tuples, podemos quebrar a arry numpy através do seus index: d = a[0:3] ==> da pos 0 até a 2
#operações basicas no numpy: são computacionalmente mais rápidas  e requerem menos memória. Adição vetorial é amplamente utilizada na ciência de dados.
#Quando eu for fazer uma operação de soma de vetor, eu somo o primeiro elemento fo vetor1 com o primeiro elemento do vetor2.
#Adicionar:
u=[1,0]
v=[0,1]
#u = np.array([1,0])
#v=np.array([0,1])
z=[]
for n,m in zip(u,v):
    z.append(n+m)

#multiplicação de array: u^T v = 1*0+0*1 = 2
#A media de todos os elementos é dada por: a.mean(), valor maximo: a.max()
#pegar valor de PI = np.pi, valor de seno = np.sin(a) ==> retorna um array com o seno de cada elemento
#Plotagem matemática: np.lienspace()
#para gerar gráficos:

#import matplotlib.pylot as plt
#%matplotlib inline
#plt.plot(x,y) ==> constroi gráficos
#transformar a lista em array:
#import numpy as np
#a=[1,2,3,4,5]
#lista = np.array(a)
#NUMPY 2D: ou seja 2 colunas
#A=np.array([[1,2],[3,4],[5,6],[7,8]]) matriz 4x4. Os valores das linhas são os primeiros valores.
#a.ndim vai ser 2
#pegar valores: A[linha][coluna]
#A[0:2,2] pegar os valoresdas duas ultimas colunas
#Na soma da matriz 2D eu faço: x[0][0]+y[0][0].
#Quando forem valores diferentes eu faço linha X coluna
#np.dot(A,B)
#Dot product of two arrays. Specifically, faz a multiplicação dos dois Arrays.
# Access the element on the first row and first and second columns
#A[0][0:2]
# Access the element on the first and second rows and third column
#A[0:2, 2]
#We use the numpy attribute T to calculate the transposed matrix
#C = np.array([[1,1],[2,2],[3,3]])
#C.T

Name="Michael Jackson"
print(Name.find('el'))

tuple1=("A","B","C" )
print( tuple1[-1])

A=((11,12),[21,22])
print(A[0][1])