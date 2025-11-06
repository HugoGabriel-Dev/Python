nascimento = int(input("ano que você nasceu: "))
idade = 2025 - nascimento
print (f"você tem {idade} anos")
if idade <= 9:
    print("categoria: MIRIM")
elif idade <= 14:
    print("categoria: INFANTIL")
elif idade <= 19:
    print("categoria: JUNIOR")
elif idade <= 25:
    print("categoria: SÊNIOR")
else :
    print("categoria: MASTER")
