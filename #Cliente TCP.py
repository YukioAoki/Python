#Cliente TCP
import socket
#Fornece acesso algumas variaveis com o interpretador
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou !!!")
        print(f"Erro foi {e}")
        sys.exit()
    print("Socket criado")
    hostalvo = input("Digite o host ou IP a ser conectado: ")
    portaalvo = int(input("Digite a porta a ser conectada: "))

    try:
        s.connect((hostalvo,portaalvo))
        print(f"Cliente TCP conectado com Sucesso no host {hostalvo} na porta {portaalvo} ")
        s.shutdown(2)
    except socket.error as e:
        print("Conexão falha")
        print(f"O erro foi {e}")
        sys.exit()

if __name__ == "__main__":
    main()
    
