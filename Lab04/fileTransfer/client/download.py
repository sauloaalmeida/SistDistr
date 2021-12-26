import applicationclientlayer as appCliLayer
import re

DOWNLOAD_PATH="/home/saulo/SistDistr/download/"

'''Metodo que valida se o usuario digitou alguma coisa ao solicitar o arquivo 
   Entrada: Nome do arquivo digitado pelo usuario
   Saida: booleano indicando que o nome veio em branco'''
def validaEntrada(msg):
    return (re.search("\w+",msg) != None )


'''Metodo que salva o conteudo do arquivo, em um novo arquivo na pasta de transferencias do lado cliente
   Entrada: Nome do arquivo, Conteudo do Arquivo
   Saida:'''
def saveFile(fileName, fileContent):
    with open(DOWNLOAD_PATH + fileName, 'w') as f:
        f.write(fileContent)

'''Metodo Principal com loop para interagir com o usuario e com tratamento das entradas do usuario
   e da excecao de arquivo inexistente
   Entrada:
   Saida:'''
def doRequests():
    #loop infinito para permitir varias operacoes do cliente
    while True:
        fileName = input('Digite o arquivo que deseja baixar, ou "fim" para encerrar:')
        
        #se vier o comando de final de uso do aplicativo, sai do loop infinito
        if fileName == "fim":
            print("\nObrigado por usar nosso aplicativo")
            break
            
        #verifica se o nome do arquivo eh valido
        if not validaEntrada(fileName):
            #se nao for valido, sai desse laço e tenta novamente
            print("Eh preciso informar o nome do arquivo!\n")
            continue
        try:
            #pega o conteudo do arquivo e salva na pasta de download
            fileContent = appCliLayer.getFileContent(fileName)
            
            #salva no diretorio de download
            saveFile(fileName, fileContent)
            print("O arquivo: {0} foi salvo no diretorio de Transferencias!\n".format(fileName))
            
        except FileNotFoundError  as err:
            #apresenta mensagem de erro para o usuario caso o arquivo nao exista
            print(err)
            
def main():
    doRequests()

main()
