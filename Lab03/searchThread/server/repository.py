from os.path import exists

#Constantes usadas no projeto
FILE_PATH="/home/saulo/SistDistr/Lab02/search/server/files/"
ERROR_MSG="Arquivo '{arquivo}' solicitado nao foi encontrado"
    
    
#metodo que retorna o conteudo do arquivo (caso exista) 
#ou uma mensagem de erro (caso nao exista    
def getContent(arq):
     fullPath=FILE_PATH + arq
     text = ""
     
     #Se o arquivo nao existir, devolve mensagem de erro
     if not exists(fullPath):
          return ERROR_MSG
     
     #se aind esta aqui, le o arquivo e devolve o conteudo
     file = open(fullPath,mode='r')
     text = file.read()
 
     #fecha o arquivo
     file.close()
     
     return text
