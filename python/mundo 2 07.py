preco = float(input('PREÇO DAS COMPRAS: R$'))
vista_cheque = (preco * 10) / 100
vistacartao = (preco * 5) / 100
duasvezes = preco / 2
tresvezesmais = (preco * 20) / 100
pcj = preco + tresvezesmais

print ("FORMAS DE PAGAMENTO: ")

print ("[1] à vista dinheiro/cheque ")
print ("[2] à vista cartão ")
print("[3] 2x no cartão ")
print("[4] 3x ou mais no cartão ")

opcao = int(input('escolha uma opção: '))

if opcao == 1:
    print(f'suas compras deram {preco}. você deve pagar {preco - vista_cheque}')
elif opcao == 2:
        print(f'suas compras deram {preco}. você deve pagar {preco - vistacartao}')
elif opcao == 3:
        print(f'suas compras deram {preco}. você deve pagar duas vezes de {duasvezes}')
elif opcao == 4:
        vezes = int(input('quantas vezes você quer parcelar? '))
        if vezes >= 3: 
            aiai = pcj / vezes 
            print(f'suas compras deram {preco}. você deve pagar {vezes} vezes de {aiai}')
        else:
             print("Número de parcelas inválido para essa opção.")
else:
    print("Opção inválida. Tente novamente.")




