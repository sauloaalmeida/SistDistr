import repository 
from repository import ERROR_MSG


def countWord(text,query):
     return text.lower().count(query.lower())

def getWordOccurences(arq, query):
     content = repository.getContent(arq)
     if content == ERROR_MSG:
     	  return content.format(arquivo = arq)
     	  
     #se ainda esta aqui, conta as palavras do conteudo do livro
     ocurrences = countWord(content, query)
     msgReturn = "A palavra '{q}' foi encontrada: '{vezes}' vezes no arquivo '{arquivo}'"

     return msgReturn.format(q=query, vezes=str(ocurrences), arquivo=arq)

#print(getWordOccurences('book01.txt','he is'))
