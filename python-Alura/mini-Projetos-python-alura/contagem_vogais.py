# Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.

# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

texto = input('Digite o texto para saber quantas vogais tem: ')

texto.lower()

contador = 0
vogais = 'aeiouáéíóúâêîôûãõ'

for letras in texto:
    if letras in vogais:
        contador += 1

print(contador)