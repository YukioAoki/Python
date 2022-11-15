#Cliente UDP
import socket

#Criado objeto de conexão.
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso")

#Definição de Host
host = '127.0.0.1'
#Definição de porta
porta = 8989
#Definição de mensagem
mensagem = 'Teste'
#Tentativa de envio e recebimento da mensagem
try:
    print(f'Cliente: {mensagem}')
    #Empacotamento da mensagem
    s.sendto(mensagem.encode(), (host,8989))
    #Espera da resposta
    dados, servidor = s.recvfrom(1024)
    #Desempacotamento do pacote
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    #Fechando a conexão
    print("Conexão fechada")
    s.close()
