#abri arquivo FILE Object
#para abrir arquivos txt, como parametro colocamos o caminho do arquivo, no segundo parametro usamos o modo "w" para esrever,
# 'r' para ler, 'a' para adicionar
#file1 = open('file.txt','w')
#podemos ver o atributo (W,R,A) que o arq tem
#print(file1.mode)
#para ler o arq é uma boa pratica usar o "with", pois ele automaticamente fecha o arq
with open("file.txt",'r') as file1:
    #linha = file1.readline()
    for linha in file1:
        print('Interaction: ',linha)
print(file1.closed)#verifica se o arq está fechado
print(file1.name)
#para ler podemos usando .readline() ou .read(), ou posso definir a qtd de linhas que ele vai ler .readlines(2)
#o .read() para de ler no primeiro espaço

# Write line to file

with open('file.txt', 'w') as writefile:
    writefile.write("This is line A")

# Read file
with open('file.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Write a new line to text file

with open('file.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")

# Verify if the new line is in the text file

with open('file.txt', 'r') as testwritefile:
    print(testwritefile.read())

#posso criar um vetor com os valores que eu quero e adicionar eles ao meu arq
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open('file.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
# Verify if writing to file is successfully executed

with open('file.txt', 'r') as testwritefile:
    print(testwritefile.read())

#Copiar um arquivo para outro, posso salvar os meus dados em difernetes formatos de arquivos ex: .txt, .csv, .xls (for excel files) etc:
# Copy file to another

with open('file.txt','r') as readfile:
    with open('file2.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


with open('file2.txt','r') as testwritefile:
    print(testwritefile.read())

with open("Example3.txt","a") as file1:

    file1.write("This is line C\n")