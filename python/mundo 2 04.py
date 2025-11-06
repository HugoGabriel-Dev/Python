pn = float(input("primeira nota: "))
sn = float(input("segunda nota: "))
media = (pn + sn) / 2

if media >= 7 :
    print ("aprovado")
elif media >= 5:
    print('recuperação ')
else :
    print ('reprovado')