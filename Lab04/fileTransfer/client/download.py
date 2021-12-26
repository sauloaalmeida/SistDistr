import applicationclientlayer as appCliLayer
import re

DOWNLOAD_PATH="/home/saulo/SistDistr/download/"

#valida os dados de entrada informado pelo usuario
def validaEntrada(msg):
    return (re.search("\w+",msg) != None )

def saveFile(fileName, fileContent):
    with open(DOWNLOAD_PATH + fileName, 'w') as f:
        f.write(fileContent)

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
