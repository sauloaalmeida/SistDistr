import repository 
from repository import ERROR_MSG


def countWord(text,query):
     return text.lower().count(query.lower())

def getWordOccurences(arq, query):
     content = repository.getContent(arq)
     if content == ERROR_MSG:
     	  return content
     	  
     #se ainda esta aqui, conta as palavras do conteudo do livro
     ocurrences = countWord(content, query)
     return "A palavra '" + query + "' foi encontrada: " + str(ocurrences) + " vezes"

#print(getWordOccurences('1-TheHungerGames.txt','hsajahskjashhkjhe'))
