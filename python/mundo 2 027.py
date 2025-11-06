soma = quant = 0

while True:
    num  = int(input("digite um numero: "))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'{quant} {soma}')