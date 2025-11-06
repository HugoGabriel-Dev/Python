
hoje = 2025
ano = int(input('ANO DO NASCIMENTO: ')) 
idade = hoje - ano
print (f'quem nasceu em {ano} tem {idade} anos em {hoje}')
alistamento = 18
qntfalta = abs(alistamento - idade) 


if idade < alistamento:
    print(f'seu alistamento será em {hoje + qntfalta}')
    print(f'ainda faltam {qntfalta} anos para se alistar ')
elif idade > alistamento:
    print(f'já deveria ter se alistado a {qntfalta} anos ')
    print(f'seu alistamento foi em {hoje - qntfalta} ')
else :
    print ('VOCÊ DEVE SER SE ALISTAR IMEDIATAMENTE! ')