import socket
import select
import sys
import threading
import service

HOST = '127.0.0.1'    # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORTA = 5001  # porta onde chegarao as mensagens para essa aplicacao
inputs = [sys.stdin] #define a lista de I/O de interesse (jah inclui a entrada padrao)
conns = {} #armazena historico de conexoes


'''Pega o conteudo do arquivo na camada de processamento (service.py)
   Entrada: o nome do Arquivo
   Saida: Conteudo do arquivo ou o conteudo "ERROR", caso o arquivo nao exista'''
def getFileContent(fileName):
    try:
        fileContent = service.fileContent(fileName)
    except FileNotFoundError:
        fileContent = "ERROR"
    return fileContent

'''Inicializa o socket inicial do lado server
   Entrada: 
   Saida: o socket inicial do lado server'''
def initializeServer():

    # cria um socket para comunicacao
    sock = socket.socket() # valores default: socket.AF_INET, socket.SOCK_STREAM  

    # vincula a interface e porta para comunicacao
    sock.bind((HOST, PORTA))

    # define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
    print('Comecou a ouvir em: ', HOST ,  ' :  ', PORTA) 
    sock.listen(5) 

    # configura o socket para o modo nao-bloqueante
    sock.setblocking(False)
    
    # inclui o socket principal na lista de entradas de interesse
    inputs.append(sock)

    #retorna o socket de conexao principal
    return sock

'''Aceita o pedido de conexao de um cliente
   Entrada: o socket do servidor
   Saida: o novo socket da conexao e o endereco do cliente'''
def acceptConn(sock):


    # estabelece conexao com o proximo cliente
    clisock, endr = sock.accept()

    # registra a nova conexao
    conns[clisock] = endr

    return clisock, endr


'''Metodo que eh executado na thread do servidor, a cada requisicao. 
   Recebe uma mensagen com o nome do arquivo e envia de volta o conteudo do arquivo para 
   o cliente (ate o cliente finalizar). Apos o envio, a conexao eh fechada para forcar o 
   envio da mensagem. Essa foi a estrategia adotada para facilitar o recebimento no loop do lado cliente.
   Envia o conteudo do arquivo solicitado para o Socket informado na entrada.
   Entrada: socket da conexao e endereco do cliente (para efeito de log)
   Saida: '''
def answeringRequests (cliSock, endr):
    #recebe dados do cliente
    data = cliSock.recv(1024)
    if not data: # dados vazios: encerra o cliente encerrou
        print(str(endr) + '-> encerrou')
        cliSock.close() # encerra a conexao com o cliente
        return 
    
    #se ainda esta aqui, atende a requisicao do cliente
    #pega a string enviada
    nomeArq = str(data, encoding='utf-8')
    
    #printa log do que esta sendo atendido
    print(str(endr) + ': ' + nomeArq)
    
    #Obtem da camada de processamento, o conteudo do arquivo
    returnMsg = getFileContent(nomeArq)
    
    #envia a resposta para o lado client 
    print("retorno Server: " + str(len(returnMsg)))
    cliSock.sendall(returnMsg.encode('utf-8'))
    
    #fecha a conexao logo apos o envio
    cliSock.close()

'''Funcao principal da rotina server. Gerencia os acessos bloqueantes dos sockets, do teclado e cria 
   instancias de execucao (com threads) para cada nova requisicao feita ao lado server.
   Entrada: 
   Saida: '''
#
def main():
    #Inicializa e implementa o loop principal (infinito) do servidor
    clients=[] #armazena as threads criadas para fazer join
    initialSock = initializeServer()
    print("Pronto para receber conexoes...")
    while True:
        #espera por qualquer entrada de interesse
        read, write, execute = select.select(inputs, [], [])
        #tratar todas as entradas prontas
        for ready in read:
            if ready == initialSock:  #pedido novo de conexao
                cliSock, endr = acceptConn(initialSock)
                print ('Conectado com: ', endr)
                #cria nova thread para atender o cliente
                client = threading.Thread(target=answeringRequests, args=(cliSock,endr))
                client.start()
                clients.append(client) #armazena a referencia da thread para usar com join()
            elif ready == sys.stdin: #entrada padrao
                cmd = input()
                if cmd == 'fim': #solicitacao de finalizacao do servidor
                    for c in clients: #aguarda todas as threads terminarem
                        c.join()
                    initialSock.close()
                    sys.exit()
                elif cmd == 'hist': #outro exemplo de comando para o servidor
                    print(str(conns.values()))

#executa o codigo do lado server
main()
