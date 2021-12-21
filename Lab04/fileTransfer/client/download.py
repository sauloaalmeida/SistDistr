import socket
import re

HOST = '127.0.0.1'  # maquina onde esta o par passivo
PORTA = 5001        # porta que o par passivo esta escutando
MAXLEN = 523003

#valida os dados de entrada informado pelo usuario
def validaEntrada(msg):
     return (re.search("\w+",msg) != None )

def receiveAll(sock):
    chunks = []
    received = 0
    while received < MAXLEN:
        chunk = sock.recv(min(MAXLEN - received, 1024))
        if not chunk:
            print('Chunk veio em branco')
            break
        chunks.append(chunk)
        received = received + len(chunk)
    return b''.join(chunks)

def initalizeClient():
    # cria socket
    initialSock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

    # conecta-se com o par passivo
    initialSock.connect((HOST, PORTA))

    return initialSock


def doRequests(sock):
    while True:
        msg = input('Informe o nome do arquivo que deseja baixar e tecle enter,  ou digite "fim" para encerrar. (Ex:book01.txt):')
        if msg == 'fim': break
        #se ainda aqui, faz a requisicao
        if validaEntrada(msg):
           sock.send(msg.encode('utf-8'))
           #espera a resposta do server conectado (chamada pode ser BLOQUEANTE)
           msgRcv = receiveAll(sock)
           
           #apresenta a resposta que veio do lado server
           print("\n" + str(msgRcv,  encoding='utf-8') + "\n" )
        else:
           print("\nEh necessario informar o nome de um arquivo para fazer o download.")
         #se foi fim, encerra o socket
    sock.close()
    print("\n Obrigado por usar a nossa ferramenta de transferencia! \n" )

def main():
    initialSock = initalizeClient()
    doRequests(initialSock)

main()
