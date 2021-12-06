import repository 
from repository import ERROR_MSG

#metodo que conta a quantidade de palavras encontradas
#pesquisa com o conteudo em minusculo, para ignorar o case sensitive
def countWord(text,query):
     return text.lower().count(query.lower())


#Solicita o conteudo do documento para a camada de servico
#Formata a mensagem de sucesso ou erro para devolver para  acamada cliente
def getWordOccurences(arq, query):

     #pega os dados do arquivo da camada de acesso a dados
     content = repository.getContent(arq)
     if content == ERROR_MSG:
     	  return content.format(arquivo = arq)
     	  
     #se ainda esta aqui, conta as palavras do conteudo do documento
     ocurrences = countWord(content, query)
     msgReturn = "A palavra '{q}' foi encontrada: '{vezes}' vezes no arquivo '{arquivo}'"

     return msgReturn.format(q=query, vezes=str(ocurrences), arquivo=arq)

