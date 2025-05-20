# Exercicio_0
ANO_ATUAL = 2025
nome = input('Qual o seu nome? ')
sobrenome = input('Qual o seu sobrenome? ')
ano_nascimento = int(input('Que ano você nasceu? '))
idade = ANO_ATUAL - ano_nascimento
print(f'Olá, {nome} {sobrenome}! Bom dia! Você possui {idade} anos!')

# exercicio_1
x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
soma = x + y
print(x if soma % 2 == 0 else y)

# exercicio_2
nota_1 = int(input('Digite a primeira nota: '))
nota_2 = int(input('Digite a segunda nota: '))
nota_3 = int(input('Digite a terceira nota: '))
nota_4 = int(input('Digite a quarta nota: '))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print('Aprovado' if media >= 7 else 'Reprovado')

# exercicio_3
temp_f = float(input('Digite a temperatura em Fahrenheit: '))
f_para_c = (temp_f - 32)/1.8
print(f'A temperatura em graus Celsius é {f_para_c:.1f}°C')

temp_c = float(input('Digite a temperatura em Celsius: '))
c_para_f = (1.8 * temp_c) + 32
print(f'A temperatura em Fahrenheit é {c_para_f:.1f}°F')

# exercicio_4
valor = float(input('Digite o valor do produto: R$ '))
print('\nFormas de pagamento:')
print('1 - PIX (15% de desconto)')
print('2 - À vista no crédito (10% de desconto)')
print('3 - Parcelado em 2x (sem juros)')
print('4 - Parcelado em 3x (10% de juros)')

metodo = int(input('\nQual a forma de pagamento? '))

if metodo == 1:
    total = valor * 0.85
    print(f'Valor total com desconto: R$ {total:.2f}')
elif metodo == 2:
    total = valor * 0.90
    print(f'Valor total com desconto: R$ {total:.2f}')
elif metodo == 3:
    print(f'2x de R$ {valor/2:.2f} (Total: R$ {valor:.2f})')
elif metodo == 4:
    total = valor * 1.10
    print(f'3x de R$ {total/3:.2f} (Total: R$ {total:.2f})')
else:
    print('Opção inválida!')

# exercicio_5
DOLAR = 5.20

def conversor(valor):
    return round(valor * DOLAR, 2) if valor >= 0 else None


    assert conversor(5) == 26.0
    assert conversor(10) == 52.0
    assert conversor(100) == 520.0
    assert conversor(2.50) == 13.0
    assert conversor(1.99) == 10.35
    print("Todos os testes do conversor passaram!")

test_conversor()
print(conversor(1.99))

# exercicio_6
def operacao(x, y, z):
    if (y * z) > x:
        return x
    elif (x + y) > z:
        return y
    elif (z - y) > x:
        return z
    else:
        return x + y + z

x = int(input('Digite um valor: '))
y = int(input('Digite um valor: '))
z = int(input('Digite um valor: '))
print(operacao(x, y, z))

# exercicio_7
def nome_do_mes(numero_mes):
    meses = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    return meses.get(numero_mes, 'Inválido')

# Teste exercicio_7
print(nome_do_mes(1))  # Janeiro
print(nome_do_mes(13)) # Inválido

# exercicio_9
def data_valida(dia, mes, ano):
    if mes < 1 or mes > 12 or ano < 0 or dia < 1:
        return False
    
    if mes == 2:
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        return dia <= 29 if bissexto else dia <= 28
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    else:
        return dia <= 31

# Teste exercicio_9
print(data_valida(29, 2, 2020))  # True (ano bissexto)
print(data_valida(29, 2, 2021))  # False

# exercicio_10
number = int(input('Digite um número positivo de até 3 dígitos: '))
    
if number < 0 or number > 999:
    print('NÚMERO INVÁLIDO')
else:
    unidade = number % 10
    dezena = (number // 10) % 10
    centena = number // 100
    print(f'Centena: {centena}')
    print(f'Dezena: {dezena}')
    print(f'Unidade: {unidade}')