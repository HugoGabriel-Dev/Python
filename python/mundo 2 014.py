termo = int(input('primeiro termo: '))
razao = int(input('razão: '))
decimo = termo + (11- 1) * razao
for i in range (termo, decimo, razao):
    print(i)
print('acabou')