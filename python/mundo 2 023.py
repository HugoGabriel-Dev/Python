def fatorial(n):
    if n < 0:
        return "Fatorial não existe para números negativos."
    
    resultado = 1
    contador = n
    while contador > 1:
        resultado *= contador
        contador -= 1
    return resultado

# Exemplo de uso:
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")
