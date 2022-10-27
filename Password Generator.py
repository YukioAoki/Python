import random
from string import punctuation
from string import digits
from string import ascii_lowercase
from string import ascii_uppercase


carac = punctuation + digits + ascii_lowercase + ascii_uppercase

num = int(input("Digite o número de senhas que você quer gerar: "))
tam = int(input("Digite a quantidade de caractéres necessário na senha: "))

for passwd in range(num):
    password = ''
    for c in range(tam):
        password += random.choice(carac)
    print(password)

