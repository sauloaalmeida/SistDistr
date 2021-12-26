#Constantes usadas no projeto
FILE_PATH="/home/saulo/SistDistr/files/"

'''Metodo que retorna o conteudo do arquivo 
   Entrada: nome do arquivo
   Saida: se o arquivo existir, retorna o conteudo (como string) de todo o arquivo
          se o arquivo nao existir, deixa vazar a exception FileNotFoundError da API do Python 
'''
def getFileContent(arq):
     fullPath=FILE_PATH + arq
     
     #le o arquivo e devolve o conteudo
     with open(fullPath, 'r') as targetFile:
         return targetFile.read()
