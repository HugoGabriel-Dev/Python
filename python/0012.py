

''' len ()--> dizer quantos carac tem a frase
count ()--> contar quantas vezes uma letra da frase apareceu 
find ()--> encontrar quantas vezes  uma determinada parte apareceu
replace ()--> substituir uma palavra da frase
upper ()--> deixar palavras e letras em maiusculo
lower ()--> deixar plavras em minusculo
capitalize ()--> deixa toda string em minusculo e apenas a primeira letrada frase em maiusculo
title ()--> capitalize, sendo que deixando todas iniciais de palavras em maiusculo 
strip ()--> elimina espaços inuteis
rstrip()--> elimina espaços somente da direta
lstrip()--> elimina espaços somente da esquerda
split()--> mata os espaços e coloca cada palavra em uma lista separada
join()--> escolho algo que quero usar para separar meu texto 
""" --> marcar para o print a string inteira '''

nome = input("digite seu nome completo: ")

maiusculo = nome.upper()
print (f"SEU NOME EM MAIUSCULO É: {maiusculo}")

minusculo = nome.lower()
print(f"SEU NOME EM MINUSCULO É: {minusculo}")

sem_espaços = nome.replace(" ", "")
sem = len(sem_espaços)
print(f"A QUANTIDADE DE CARACTERES DO SEU NOME É : {sem}")

letras = nome.split()
primeiro = len(letras[0])
print (f"SEU PRIEMIRO NOME TEM EM LETRAS: {primeiro}")