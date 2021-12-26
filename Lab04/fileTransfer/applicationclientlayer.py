import socket

HOST = '127.0.0.1'  # maquina onde esta o par passivo
PORT = 5001        # porta que o par passivo esta escutando

#trata o recebimento do socket no loop
def receiveAll(sock, msgSize):
    chunks = []
    received = 0
    while received < msgSize:
        chunk = sock.recv(min(msgSize - received, 1024))
        if not chunk:
            print('Chunk veio em branco')
            break
        chunks.append(chunk)
        received = received + len(chunk)
    return b''.join(chunks)

#metodo que obtem o tamanho do arquivo
#Lanca excecao caso o arquivo nao exista (tamanho do arquivo ==-1)
#fecha a conexao logo apos retornar o tamanho do arquivo
def getFileSize(fileName):
    with socket.socket() as sock:
        sock.connect((HOST, PORT))
        #formata a mensagem com o metodoDesejado,nomeArquivo
        #ex: fileSize,book01.txt
        msg="fileSize,"+fileName
        sock.sendall(msg.encode("utf-8"))
        msgRcv = sock.recv(1024)
        fileSize = int(str(msgRcv,  encoding='utf-8'))
        if fileSize < 0:
            raise FileNotFoundError("O arquivo '{0}' nao existe!".format(fileName))
        return fileSize

#metodo que obtem o conteudo do arquivo
#fecha a conexao logo apos retornar o conteudo do arquivo
def getFileContent(fileName):
    #para pegar todo o conteudo, primeiro obtem o tamanho do arquivo
    fileSize = getFileSize(fileName)
    
    with socket.socket() as sock:
        sock.connect((HOST, PORT))
        #formata a mensagem com o metodoDesejado,nomeArquivo
        #ex: fileSize,book01.txt
        msg="fileContent,"+fileName
        sock.sendall(msg.encode("utf-8"))
        msgRcv = receiveAll(sock, fileSize)
        return str(msgRcv,  encoding='utf-8')
