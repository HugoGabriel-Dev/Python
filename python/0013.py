
''' len ()--> dizer quantos carac tem a frase
count ()--> contar quantas vezes uma letra da frase apareceu 
find ()--> encontrar quantas vezes uma determinada parte apareceu
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

num = int(input("DIGITE UM NÚMERO DE (1 a 99999): "))

if 1 <= num <= 99999:
    print(f"Número digitado: {num}")

    # Garante que tenha 5 dígitos
    n = str(num).zfill(5)

    uni_milhar = int(n[0]) 
    milhar = int(n[1])
    centena = int(n[2])
    dezena = int(n[3])
    unidade = int(n[4])

    print (f"UNIDADE DE MILHAR: {uni_milhar}")
    print(f"MILHAR : {milhar}")
    print(f"CENTENA: {centena}")
    print(f"DEZENA : {dezena}")
    print(f"UNIDADE: {unidade}")

else:
    print("⚠️ O número não está dentro das normas (1 a 9999).")



