salario = float(input('digite seu salario: '))
porct1 = (salario * 10) / 100
porct2 = (salario * 15) / 100
nsalario = salario + porct2
nsalarioo = salario + porct1

if salario <= 1251.00 :
    print (f'seu novo salario: {nsalario}')
else: 
    print (f'seu novo salario: {nsalarioo}')