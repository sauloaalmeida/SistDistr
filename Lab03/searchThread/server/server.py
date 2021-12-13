import socket
import service

HOST = ''    # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORTA = 5000  # porta onde chegarao as mensagens para essa aplicacao

# cria um socket para comunicacao
sock = socket.socket() # valores default: socket.AF_INET, socket.SOCK_STREAM  

# vincula a interface e porta para comunicacao
sock.bind((HOST, PORTA))

# define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
print('Comecou a ouvir em: ', HOST ,  ' :  ', PORTA) 
sock.listen(5) 

# aceita a primeira conexao da fila (chamada pode ser BLOQUEANTE)
novoSock, endereco = sock.accept() # retorna um novo socket e o endereco do par conectado
print ('Conectado com: ', endereco)

while True:
     # depois de conectar-se, espera uma mensagem (chamada pode ser BLOQUEANTE))
     msg = novoSock.recv(1024) # argumento indica a qtde maxima de dados
     if not msg or str(msg,  encoding='utf-8') == 'fim':
          break
     else:
          msgStr=str(msg,  encoding='utf-8')
          print(msgStr)
          
          #separa os parametros da busca (arquivo e query)
          arq,query = msgStr.split(',')
          
          msgReturn = service.getWordOccurences(arq, query)
          novoSock.send(msgReturn.encode('utf-8'))

# fecha o socket da conexao
novoSock.close() 

# fecha o socket principal
sock.close() 
