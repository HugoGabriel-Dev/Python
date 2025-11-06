from random import randint

sorteio = randint(0, 10)
acertou = False
tentativas = 0

while not acertou:
    num = int(input("Tente adivinhar o número que escolhi de 0 a 10: "))
    tentativas += 1
    if num == sorteio:
        acertou = True
        print(f"Parabéns! Você acertou o número {sorteio} com {tentativas} tentativa(s)!")
    else:
        if num > sorteio:
            print('menos')
        elif num < sorteio:
            print ("mais")
