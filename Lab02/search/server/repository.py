from os.path import exists

FILE_PATH="/home/saulo/SistDistr/Lab02/search/server/files/"
ERROR_MSG="Arquivo solicitado nao foi encontrado"
    
def getContent(arq):
     fullPath=FILE_PATH + arq
     text = ""
     
     if not exists(fullPath):
          return ERROR_MSG
     
     #se aind esta aqui, le o arquivo e devolve o conteudo
     file = open(fullPath,mode='r')
     text = file.read()
 
     #fecha o arquivo
     file.close()
     
     return text
     



#print(getContent('Little-Prince-final-text.pdf'))

