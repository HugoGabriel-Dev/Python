import math

co = float(input("escreva o valor do cateto oposto "))
ca = float(input("escreva o valor do cateto adjacente "))
hip = math.hypot (co, ca)
print(f"SUA HIPOTENUSA É IGUAL A {hip:.2f}")
