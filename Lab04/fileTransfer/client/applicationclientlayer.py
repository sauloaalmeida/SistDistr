import socket

HOST = '127.0.0.1'  # maquina onde esta o par passivo
PORT = 5001        # porta que o par passivo esta escutando


'''Metodo que retorna o conteudo consolidadodo com um loop no receive do socket 
   Entrada: o socket que se deseja obter o receive
   Saida: O conteudo em bytes consolidado apos o loop
'''
def receiveAll(sock):
    chunks = []
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            #sai do loop de recebmento pois a conexao foi fechada. Indica final do arquivo
            break
        chunks.append(chunk)
    return b''.join(chunks)

'''Metodo que envia a mensagem com o nome do arquivo e recebe o conteudo. Caso venha o texto de erro, 
   lanca a excecao informando que o arquivo nao existe
   Entrada: Nome do Arquivo
   Saida: Conteudo do arquivo, ou excecao inficando que o arquivo nao existe, para ser tratado na 
   camada de interface com o usuario'''
def getFileContent(fileName):
    with socket.socket() as sock:
        sock.connect((HOST, PORT))
        #manda o nome do arquivo
        sock.sendall(fileName.encode("utf-8"))
        msgRcv = receiveAll(sock)
        fileContent = str(msgRcv,  encoding='utf-8')
        if(fileContent ==  "FILE_NOT_FOUND"):
            raise FileNotFoundError("O arquivo '{0}' nao existe!\n".format(fileName))
        return fileContent
