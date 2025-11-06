

def fatorial (n):
    f = 1
    for i in range (1, n+1):
        f*=i
    return f

# programa principal
num = int(input("digite um numero: "))
fat = fatorial(num)
print(f'o fatorial de {num} é {fat}')