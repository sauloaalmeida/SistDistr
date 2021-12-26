import repository

#Solicita o conteudo do documento para a camada de servico
def fileContent(arq):
    #retorna o conteudo do arquivo para o server
    return repository.getFileContent(arq)
