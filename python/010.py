import math

ang = float(input("DIGITE O ANGULO EM (RAD) QUE VOCÊ DESEJA SABER O SEN, COS, TAN? "))

graus = math.radians(ang)


sen = math.sin(graus)
cos = math.cos(graus)
tan = math.tan (graus)

print (f"SEU SENO É: {sen:4f}")
print (f"SEU COS É: {cos:.4f}")
print (f"SUA TAN É: {tan:.4f}")





