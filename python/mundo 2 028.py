while True:
    n = int(input('quer ver a tabuada de q numero? '))
    if n < 0:
          print('vc so pode ser burro!')
          break
    for num in range (1, 11):
            resultado = n * num 
            print (f" {n} x {num} = {resultado}")



