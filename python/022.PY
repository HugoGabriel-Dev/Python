dis = int(input('DIGITE QUAL FOI A DISTANCIA DA SUA VIAGEM EM (KM): '))
duzentos = dis * 0.50
depois = dis * 0.45

if dis <= 200 :
    print(f'TOTAL: {duzentos}')
else :
    print(f'TOTAL: {depois}')