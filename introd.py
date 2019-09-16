print("Hello \nWord")
#conversao de valores
int(1.0)
#bool = True or bool = False
#bool(1) => TRue
#bool(0) => False
#Exressoes = operações que o Python realiza.
# Em python 3 as divisões sempre dão float, para ter um resultado inteiro, eu uso as "//"
#Em relação a isso o python em expressões ele segue a regra de multiplicacao e divisao antes de subtracao e soma

import sys
print(sys.version)
#Strings sao imutáveis
#nome.find('laura') => ve se na string tem a palavra laura
#nome.replace('a','A') => troca todos os valor a por A
#Numbers[::2] => o segundo valor nao é impresso
name = "0123456"
#Filtrar os valores que irão aparecer para o usuario
print(name[::2])
print(name.find('1'))

#selecionar uma parte da mensagem
name = 'Lizz'
print(name[0:2])

#TUPLES
#Tuples sÃo sequencias ordenadas, sao definidas por "( )" com valores separados por ","
#Varios tipos de dados podem estar em uma tupla, e o tipo desses dados será "tupla", cada elemento dessa tabela pode ser acessado pelo indice
#Nos podemos concatenar ou combinar, adicionando mais elementos ao tuple
#Sao imutáveis, ou seja não podemos muda-las. Ou seja quando pegamos um valor do indice, nós nao estamos apontando para o valor, mas sim para a tupla.
tuple1 = ('disco',10,1.9)
tuple2 = tuple1 + ('banana',20.32)
print(tuple2)
#Podemos também dividir as tuplas, pegando somente alguns elementos desejados
print(tuple2[:3]) #pegar valores do indice 0 até o 2
#pegar Index
tuple1.index('disco')
#LISTAS
#Também sao de sequencia ordenada. Sao definidas pelos "[ ]" com valores separados por "," => pode conter valores de vários tipos
#Os valores podem ser acessados  pelo indice, podemos fatiar a lista tb:
L = ["Jennifer Lawrence", 20, 99.8]
print(L[1:3]) #=> pegar os ultimos elementos
#TB podemos concatenar as listas. Diferente das tuples, as listas são mutáveis
L.extend(["pop", 90]) #adiciona uma lista
L.append(["pop",90]) #adiciona um valor a lista
print(L)
#Posso transformar um tuple em lista
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)
RatingsSorted
#Posso alterar o valores na lista original tb
L[0] = "Michael Jackson"
print(L)
#Podemos usar a função split para separar a string pelo caractere delimitado especifico.
frase = "A,B,C,D,E"
frase2 = frase.split(",")
print(frase2) # cria uma lista nova com as strings quebradas
#Quando dizemos novafrase = frase2, estamos falando que a frase2 e a novafrase estão apontando para a mesma lista
#Podemos clonar a lista através da seguinte sintaxe novafrase = frase2[:] => crio uma nova lista com os mesmos dados da lista frase2
#Entretanto se eu alterar algo em qualquer uma das listas, ela não afeta a outra =)

#SETS
#São tipos de coleção. Ou seja é bem parecido com tuples e listas, entretanto eles não são ordenados.
#Isto quer dizer qu o conjunto nao registra a posição dos dados. Eles só tem elementos exclusivos. Para definir um "set" você declara "{ }" com valores separados em ","
#você pode converter uma lista usando a expressão "Setlis = set(list)". Para adicionar um elemento: A.add("ValorNovo")
# Para remover A.remove(ValorRetirado)
A = {'a','b','c'}
B = {'c','b','z'}
A.add('d') #adicionar
A.remove("c")
print(A)
#Achar a diferença entre os sets album_set1.difference(album_set2)
# Para verificar se o elemento está no Set: ""ValorPesquisado" in A , se estiver retorna True, se não tiver False
#A interseccao de dois sets é um novo set contendo elementos que estejam nos dois sets anteriores.
#A intersecção do sets é definida com a operação "and", ou seja definimos a uniao dos sets.
# set3 = set1 & set2
#Podemos tb unir/juntar os dois sets
#set1.union(set2)
#Podemos pergntar se um set é subset de outro através da expressao: set3.issubset(set1) retornando  TRue or False

#DICIONARIOS
#Tipo de coleção em python. A diferença entre listas e dicionários é que uma lista tem elementos, já um dicionário tem chaves e valores.
#A chave é uma analogia ao index, sendo o endereço do valor, sendo que a chave não precisa ser um inteiro, ultimamente são caracteres
#Os valores são similares aos elementos que contém informação em uma lista
#Para criar um dicionário usamos: {chave:valor, chave:valor }, as chaves precisam ser imutáveis e únicas
#Os valores podem ser imutáveis, mutáveis e duplicados. Por exemplo: o titulo do album é a chave e os valores são as datas # de lançamento.
#Para procurar um valor usamos DICT[CHAVE] ==> a saida é um valor
#Para adicionarmos DICT['CHAVE'] = 'VALOR'
#Para deletar: del(DICT[CHAVE# ])
#Para verificar se o valor está lá 'CHAVE' in DICT => retorna True or False
#Para pegar todas as chaves DICT.key() ==> A saida é uma lista
#Para pegar todos os valores DICT.values()

#Condição e Ramificação
# a = 6 ==> atribuindo valores
# a==6 ==> compara para ver se os valores são iguais
#comparar strings "ola" == "oi"
#Branching ou Ramificação nos permite executar instruções diferentes para cad entrada diferente.
#if(condiction):
#else:
#elif():
#Loops
#range ==> função que produz uma sequencia ordenada como uma lista "i". Começando com 0.
#range(N) ==> saida: [0,...,N-1] exemplo range(3) saida: 0,1,2
#posso definir limites: RANGE(10,15) saida 10,11,12,13,14
#for i in range(vector):
#do
a=['a','b','c']

for i in a:
    print(i)

#usar enumerate(vetor) quando quiser pegar o index e valor da pos
for i, data in a:
    print(i,data)
#FUNÇÕES  => SAO UM PEDAÇO DE CÓDIGO QUE VC PODE REUTILIZAR
#Funções built-in, o python tem muitas, vc nao precisa entender como elas foram feitas, mas sim como ela funciona(parametros e retorno).
# Sorted vs Sort ==> a função Sorted retorna uma ova lista com os dados ordenados, sem alterar a lista original. ex:
album = [1982,123,54444,2392]
album_sorted = sorted(album)
print(album_sorted)
#Já no Sort eu altero a lista original:
album.sort()
print(album)
#Para definir uma função colocamos "def". exemplo:
b=5
c=8
def add(b,c):
    b = c+1
    return b

#passar tuple como parametros *name, lista como parametro namelist
#variaveis globais podem ser usadas por qualquer metodo

#OBJeto: all objeto tem ==> um tipo, uma representação interna, um conunto de funções chamado métodos para interagir com os dados.
# Um objeto é uma instância de um tipo específico
#Metodos:: uma classe ou tipo de métodos são funções que todas as instâncias dessa classe ou tipo fornecem. É coo vc interage com o objeto
#Classe: os atributos de uma classe definem ela, definida pelo termo (class nome(object):), o object é a classe pai
#para inicializar as instancias do objeto, usamos def __init__, entao quando criarmos um objeto ele terá todos os atributo necessários
class circle(object):
    def __init__(self,radius, color):
        self.radius = radius
        self.color = color

#para criar um objeto:
Circle = circle(10,'blue')
#aceesar valores do objeto: objeto.atributo
#dir(nameobect)==> retorna uma lista com metodos atributos de um objeto especifico