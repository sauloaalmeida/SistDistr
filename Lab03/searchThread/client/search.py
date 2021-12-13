import socket
import re

HOST = '127.0.0.1'  # maquina onde esta o par passivo
PORTA = 5001        # porta que o par passivo esta escutando

#valida os dados de entrada informado pelo usuario
def validaEntrada(msg):
     return (re.search("\w+,\w+",msg) != None and msg.count(',') == 1)


def initalizeClient():
    # cria socket
    initialSock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

    # conecta-se com o par passivo
    initialSock.connect((HOST, PORTA))

    return initialSock


def doRequests(sock):
    while True:
        msg = input('Informe o nome do arquivo, e a palavra que deseja pesquisar (separado por virgula) e tecle enter,  ou digite "fim" para encerrar. (Ex:book01.txt,master):')
        if msg == 'fim': break
        #se ainda aqui, faz a requisicao
        if validaEntrada(msg):
           sock.send(msg.encode('utf-8'))
           #espera a resposta do server conectado (chamada pode ser BLOQUEANTE)
           msgRcv = sock.recv(1024) # argumento indica a qtde max de bytes da msg
           
           #apresenta a resposta que veio do lado server
           print("\n" + str(msgRcv,  encoding='utf-8') + "\n" )
        else:
           msgErro="\nA entrada '{ent}', nao esta no formato esperado."
           print(msgErro.format(ent=msg))
         #se foi fim, encerra o socket
    sock.close()
    print("\n Obrigado por usar a nossa busca! \n" )

def main():
    initialSock = initalizeClient()
    doRequests(initialSock)

main()
