from PyPDF2 import PdfFileReader
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
     


def getPdfContent(arq):
     fullPath=FILE_PATH + arq
     text = ""
     
     if not exists(fullPath):
          return ERROR_MSG
     else:     
          with open(fullPath, 'rb') as f:
               pdf = PdfFileReader(f)
               info = pdf.getDocumentInfo()
               numberOfPages = pdf.getNumPages()
               for pageNumber in range(numberOfPages):
                    page = pdf.getPage(pageNumber)
                    text += page.extractText()
               return text
                  
        
#print(getContent('Little-Prince-final-text.pdf'))

