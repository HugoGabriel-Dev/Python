from random import randint
sorteio = randint(0,5)
num = int(input("tente advinhar o numero que escolhi de 0:5? "))
print('você acertou' if num == sorteio else 'você errou!, o numero era ' , sorteio)

