ano = int(input("Digite um ano: "))

# Um ano é bissexto se:
# - for divisível por 4
# - mas não pode ser divisível por 100, exceto se também for divisível por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

