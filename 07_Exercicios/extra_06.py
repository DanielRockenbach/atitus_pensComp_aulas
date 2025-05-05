def valor_pgto(valor, forma_pgto):
    valor =  float(input('Digite o valor do produto'))

    print('Formas de pagamento:')
    print('1 - PIX')
    print('2 - A vista no Crédito')
    print('3 - Parcelado em 2x no Crédito')
    print('4 - Parcelado em 3x no crédito')

    metodo = int(input('Qual a forma de pagamento'))

    if metodo == 1:
        resultado = valor - (valor*(15/100))
        print(f'Valor total com desconto de 15%: {resultado}')
    if metodo == 2:
        resultado = valor - (valor*(10/100))
        print(f'Valor total com desconto de 10%: {resultado}')
    if metodo == 3:
        resultado = valor 
        print(f'Valor total parcelado em 2x sem juros')
    if metodo == 4:
        resultado = valor + (valor*(10/100))
        print(f'Valor total parcelado em 3x ou mais com juros de 10% {resultado}')
    else:
        print(f'Opção invalida, escolha uma opção valida.')
    


assert valor_pgto(100, 1) == 85
assert valor_pgto(100, 2) == 90
assert valor_pgto(100, 3) == 100
assert valor_pgto(100, 4) == 110
