import os

print("-" *58)
#Variável que terá o alvo do ping
ip_alvo = input("Digite o IP ou Host a ser verificado: ")

os.system(f'ping -n 6 {ip_alvo}')

print("-" *58)