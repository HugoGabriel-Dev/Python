def Cifra_cesar(text, shift, direction=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if direction:
        shift_alphabet = alphabet[shift:] + alphabet[:shift]
    else:
        shift_alphabet = alphabet[-shift:] + alphabet[:-shift]
    translation = str.maketrans(alphabet + alphabet.upper(), shift_alphabet + shift_alphabet.upper())
    return text.translate(translation)

print(Cifra_cesar('Hugo', 3, True))
print(Cifra_cesar('Kxjr', 3, False))