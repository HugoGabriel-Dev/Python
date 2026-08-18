temp = input("Digite uma temperatura: ")
temp_format = float(temp)

if(temp_format > 30):
    print(f"Está muito quente, {temp_format}")
elif(temp_format > 20):
    print(f"Está agradável, {temp_format}")
elif(temp_format > 10):
    print(f"Está frio, {temp_format}")
else:
    print(f"Frio para um caramba, {temp_format}")