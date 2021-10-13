import threading
from socket import *
serverName = 'localhost'
serverPort = 12000

nickname = input('Escolha um nickname: ')

clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverName,serverPort))
except:
    print('A conexão não foi possível no momento.')


def receive():
    while 1:
        try:
            mensagem = clientSocket.recv(1024)
            if str(mensagem.decode())=='getUser':
                clientSocket.send(nickname.encode())
            else:
                 print(mensagem.decode())
        except:
            print('Erro')
            break;

def write():
    while 1:
        clientSocket.send(input().encode())
        
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()