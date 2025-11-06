tri = int(input("coloque a medida dos lados: "))
trii = int(input("coloque a medida dos lados: "))
triii = int(input("coloque a medida dos lados: "))

if (tri + trii > triii) and (trii + triii > tri) and (triii + tri > trii):
    print('É UM TRIÂNGULO! ')
else:
    print('NÃO É UM TRIANGULO! ')

'''
a + b > c  
a + c > b  
b + c > a

'''


