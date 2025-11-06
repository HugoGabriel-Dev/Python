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
rfind()--> contar da direita pra esquerda
 --> marcar para o print a string inteira '''



nome = str(input("DIGITE SEU NOME COMPLETO: ")).strip().split()

pn = (nome[0])
print(f'SEU PRIMEIRO NOME É: {pn}')

un = (nome[-1] )
print(f"seu ultimo nome é: {un}")