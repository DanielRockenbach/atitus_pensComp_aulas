<<<<<<< HEAD
def valor_pgto(valor, forma_pgto): #Extra 06  
    if forma_pgto == 1:
        return valor - (valor * (15 / 100))
    elif forma_pgto == 2:
        return valor - (valor * (10 / 100))
    elif forma_pgto == 3:
        return valor
    elif forma_pgto == 4:
        return valor + (valor * (10 / 100))
    elif forma_pgto not in [1, 2, 3, 4]:
        return "Opção inválida. Por favor, escolha uma das opções listadas.")
=======
def valor_pgto(valor, forma_pgto):
    valor =  float(input('Digite o valor do produto'))
>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2

<<<<<<< HEAD
def test():
    assert valor_pgto(100, 1) == 85
    assert valor_pgto(100, 2) == 90
    assert valor_pgto(100, 3) == 100
    assert valor_pgto(100, 4) == 110
=======
    print('Formas de pagamento:')
    print('1 - PIX')
    print('2 - A vista no Crédito')
    print('3 - Parcelado em 2x no Crédito')
    print('4 - Parcelado em 3x no crédito')
>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2

<<<<<<< HEAD
=======
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

>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2