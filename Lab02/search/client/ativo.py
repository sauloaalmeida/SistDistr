# Exemplo basico socket (lado ativo)

import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock.connect((HOST, PORTA))

msg = ""

while msg != "fim":
     print('Digite uma mensagem para enviar, ou "fim" para encerrar')
     msg = input()
     if msg != 'fim':
          sock.send(msg.encode('utf-8'))
          #espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
          msgRcv = sock.recv(1024) # argumento indica a qtde max de bytes da msg
          print(str(msgRcv,  encoding='utf-8'))
     else:     
          # encerra a conexao
          sock.close() 
