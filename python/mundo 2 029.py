from random import randint

vitorias = 0

while True:
    valor = int(input('diga um valor: '))
    esc = str(input('quer IMPAR/PAR (P/I)? ')).upper().strip()[0]
    computador = randint(0, 10)
    soma = abs(valor + computador)

    
    print(f'você jogou {valor} e o computador {computador}. o total de {soma} DEU PAR')
    print('-=' * 40)
    if valor == 0 :
     print(f'você jogou {valor} e o computador {computador}. o total de {soma} DEU IMPAR')
     print('-=' * 40)
    if (esc == 'P' and soma % 2 == 0) or (esc == 'I' and soma % 2 != 0):
        print("VOCÊ VENCEU! ")
        vitorias += 1
        print('-=' * 40)
    else:
        print('VOCÊ PERDEU! ')
        print('-=' * 40)
        break
print(f'{vitorias} vitorias! ')

    