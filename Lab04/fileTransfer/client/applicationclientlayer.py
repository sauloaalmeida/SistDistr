import socket

HOST = '127.0.0.1'  # maquina onde esta o par passivo
PORT = 5001        # porta que o par passivo esta escutando

def receiveAll(sock):
    chunks = []
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            #sai do loop de recebmento pois a conexao foi fechada. Indica final do arquivo
            break
        chunks.append(chunk)
    return b''.join(chunks)

def getFileContent(fileName):
    with socket.socket() as sock:
        sock.connect((HOST, PORT))
        #manda o nome do arquivo
        sock.sendall(fileName.encode("utf-8"))
        msgRcv = receiveAll(sock)
        fileContent = str(msgRcv,  encoding='utf-8')
        if(fileContent ==  "ERROR"):
            raise FileNotFoundError("O arquivo '{0}' nao existe!\n".format(fileName))
        return fileContent
