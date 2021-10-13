import threading
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen()

print('The server is ready to receive')

users = []
nicknames = []

def broadcast(mensagem):
    for user in users:
        user.send(mensagem)

def handle(user):
    while 1:
        try:
            mensagem = user.recv(1024).decode()
            broadcast(f'{nicknames[users.index(user)]}: {mensagem}'.encode())
        except:
            index = users.index(user)
            users.remove(user)
            user.close()
            nickname = nicknames[index]
            print(f'{nickname} saiu do chat')
            broadcast('{nickname} saiu do chat'.encode())
            nicknames.remove(nickname)
            break

def receive():
    while 1:
        try:
            user, addr = serverSocket.accept()
            print(f'Conectado com {addr}')        
            user.send('getUser'.encode())
            nickname = user.recv(1024).decode()
            nicknames.append(nickname)
            users.append(user)
            
            print(f'{nickname} adicionado')
            broadcast(f'{nickname} entrou no chat'.encode())
            
            thread = threading.Thread(target=handle, args=(user,))
            thread.start()
        except:
            pass

receive()