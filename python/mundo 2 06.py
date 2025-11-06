tri = int(input("coloque a medida dos lados: "))
trii = int(input("coloque a medida dos lados: "))
triii = int(input("coloque a medida dos lados: "))
if (tri + trii > triii) and (trii + triii > tri) and (triii + tri > trii):
    print('É UM TRIÂNGULO! ')

    if (tri == trii == triii):
        print("equilátero ")
    elif (tri == trii) or (trii == triii) or (tri == triii):
        print('isóceles')
    else :
        print('escaleno')
else :
    print ("NÃO É TRIANGULO!")
