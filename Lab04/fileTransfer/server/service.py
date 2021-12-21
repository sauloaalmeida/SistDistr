import repository 
from repository import ERROR_MSG


#Solicita o conteudo do documento para a camada de servico
#Formata a mensagem de sucesso ou erro para devolver para a camada cliente
def getTextFile(arq):

    #pega os dados do arquivo da camada de acesso a dados
    content = repository.getContent(arq)
    if content == ERROR_MSG:
        return content.format(arquivo = arq)

    #se ainda esta aqui, retorna o conteudo do arquivo para o server
    return content

