vel = float(input("DIGITE SUA VELOVIDADE: "))
multa = 7 * (vel - 80)

if vel >= 81:
    print ('você foi multado! ')
    print ('VALOR DE $7,OO POR KM A MAIS: ')   
    print(f'você teve uma multa de: {multa} reais ')  
else:
    print('você não foi multado! ')
      
      
      
