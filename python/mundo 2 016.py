frase = str(input('digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for i in range (len(junto)-1,-1,-1):
    inverso += junto[i]
print(junto, inverso , end = '')
