print("Bem vindo ao sistemas de notas. \n")

nota = input(f"Digite a sua primeira nota: ")
nota2 = input(f"Digite a sua segunda nota: ")

nota_indentada = int(nota)
nota_indentada2 = int(nota2)
media = (nota_indentada + nota_indentada2) / 2

if media >= 7:
    print(f'Meus parabéns, você foi aprovado com media {media}!')
else:
    print(f'Que ruim, Você reprovado com media {media}!')