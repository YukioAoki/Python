import os 
import time
# Desenvolvido por Eduardo Yukio Aoki 
# Ajuda do curso de Segurança da Informação com Python

def host_escanear():
    host = input("Digite o alvo que quer escanear ou exit para sair: ")
    hosts.append(host)
    while host != "exit":
        print(hosts)
        return host_escanear()
    for ip in hosts:
        print("_" *58)
        os.system(f'ping -n 3 {ip}')
        time.sleep(2)
        print("_" *58)

print("Bem vindo ao aplicativo de teste de ping único e multiplo")
print("_" *58)
a = int(input("Digite 1 para ping único e 2 para ping múltiplo: "))
print("_" *58)

if a == 1:
    print("_" *58)
    ip_alvo = input("Digite o alvo do seu ping: ")
    os.system(f'ping -n 3 {ip_alvo}')
    print("_" *58)
elif a == 2:
    hosts = []
    host_escanear()
else: 
    print("Opção Inválida")