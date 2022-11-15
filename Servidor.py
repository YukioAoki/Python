#Irá se conectar no cliente UDP
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso')

host = 'localhost'
porta = 5982

s.bind((host, porta))
mensagem = 'Servidor Online'

while 1:
    dados, enc = s.recvfrom(1024)
    if dados:
        s.sendto(dados + (mensagem.encode()), end)