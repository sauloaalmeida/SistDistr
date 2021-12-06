import socket
import re

#valida os dados de entrada informado pelo usuario
def validaEntrada(msg):
     return (re.search("\w+,\w+",msg) != None and msg.count(',') == 1)


HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock.connect((HOST, PORTA))

msg = ""

while msg != "fim":
     print('Informe o nome do arquivo, e a palavra que deseja pesquisar (separado por virgula) e tecle enter,  ou digite "fim" para encerrar. (Ex:book01.txt,master):')
     msg = input()
     if msg != 'fim':
          if validaEntrada(msg):
               sock.send(msg.encode('utf-8'))
               
               #espera a resposta do server conectado (chamada pode ser BLOQUEANTE)
               msgRcv = sock.recv(1024) # argumento indica a qtde max de bytes da msg
               
               #apresenta a resposta que veio do lado server
               print("\n" + str(msgRcv,  encoding='utf-8') + "\n" )
          else:
               msgErro="\nA entrada '{ent}', nao esta no formato esperado."
               print(msgErro.format(ent=msg))
     else:     
          # encerra a conexao
          sock.close() 
          print("\n Obrigado por usar a nossa busca! \n" )
