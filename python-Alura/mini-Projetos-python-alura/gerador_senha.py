# Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

# Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

import random

maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
especiais = "!@#$%&*()_+"

senha = [
    random.choice(maiusculas),
    random.choice(minusculas),
    random.choice(numeros),
    random.choice(especiais)
]

todos_caracteres = maiusculas + minusculas + numeros + especiais

for _ in range(8):
    caractere_aleatorio = random.choice(todos_caracteres)
    senha.append(caractere_aleatorio)

random.shuffle(senha)

senha_final = "".join(senha)

print(senha_final)