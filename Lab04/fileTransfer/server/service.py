import repository

'''Metodo que retorna o conteudo do arquivo da camada de acesso a dados (repository) 
   Entrada: nome do arquivo
   Saida: se o arquivo existir, retorna o conteudo (como string) de todo o arquivo
          se o arquivo nao existir, deixa vazr a exception FileNotFoundError da API do Python 
'''
def fileContent(arq):
    #retorna o conteudo do arquivo para o server
    return repository.getFileContent(arq)
