# Exercicio_0

ANO_ATUAL = 2025


def saudacao(nome, sobrenome, ano_nascimento):
    if not (0<=ano_nascimento<ANO_ATUAL)
        return None
    idade = ANO_ATUAL - int(ano_nascimento)
    return f'Olá,{nome} {sobrenome}. Bom dia! Você possuí {idade} anos!'

Def test():
    assert (
        saudacao("Matheus", "Jardim", 1991)
        == "Olá, Matheus Jardim. Bom dia! Você possui 33 anos!"
    )
    assert (
        saudacao("Thais", "Silva", 1990)
        == "Olá, Thais Silva. Bom dia! Você possui 34 anos!"
    )
    assert saudacao("Matheus", "Jardim", 0) is None
    assert saudacao("Matheus", "Jardim", 2050) is None

# exercicio_1

x = int(input('Digite um valor'))
y = int(input('Digite outro valor'))

soma = x+y

if soma % 2 == :
    print(x)
else:
    print(y)

# exercicio_2

nota_1 = int(input('Digite a primeira nota')
nota_2 = int(input('Digite a segunda nota')
nota_3 = int(input('Digite a Terceira nota')
nota_4 = int(input('Digite a Quarta nota')

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7
    print('Aprovado')
else:
    print('Reprovado')


# exercicio_3

temp_f = float(input('Diga a temperatura em Fahrenheit'))
f_para_c = (temp_f - 32)/1.8
print('A temperatura em graus Celcius é' f_para_c 'C°')

temp_c = float(input('digite a temperatura em Celcius'))
c_para_f = (1.8* temp_c) + 32
print('A temperatura em Farenheit é', c_para_f, 'F°')

# exercicio_4

valor =  float(input('Digite o valor do produto'))

print('Formas de pagamento:')
print('1 - PIX')
print('2 - A vista no Crédito')
print('3 - Parcelado em 2x no Crédito')
print('4 - Parcelado em 3x no crédito')

formas_pgto = int(input('Qual a forma de pagamento'))

if forma_pgto == 1:
    resultado = valor - (valor*(15/100))
    print(f'Valor total com desconto de 15%: {resultado}')
if forma_pgto == 2
    resultado = valor - (valor*(10/100))
    print(f'Valor total com desconto de 10%: {resultado}')
if forma_pgto == 3
    resultado = valor 
    print(f'Valor total parcelado em 2x sem juros')
if forma_pgto == 4
    resultado = valor + (valor*(10/100))
    print(f'Valor total parcelado em 3x ou mais com juros de 10% {resultado}')
else:
    print(f'Opção invalida, escolha uma opção valida.')

# exercicio_5

DOLAR = 5.20
def conversor float(valor,):
    if valor<0
        return None
    resultado = (valor * DOLAR)
    return resultado{:.2f}

def test():
    assert conversor(5) == 26
    assert conversor(10) == 52
    assert conversor(100) == 520
    assert conversor(2.50) == 13
    assert conversor(1.99) == 10.34

# exercicio_6

def operacao(x, y, z):
    if (y * z) > x:
        return x
    if (x + y) > z:
        return y
    if (z - y) > x:
        return z
    else:
        print(x+y+z)

x = int(input('Digite um valor'))
y = int(input('Digite um valor'))
z = int(input('Digite um valor'))
print(operacao(x, y, z))

# exercicio_7

def nome_do_mes(numero_mes):
    if numero_ mes == 1
        return 'Janeiro'
    if numero_ mes == 2
        return 'Fevereiro'
    if numero_ mes == 3
        return 'Março'
    if numero_ mes == 4
        return 'Abril'
    if numero_ mes == 5
        return 'Maio'
    if numero_ mes == 6
        return 'Junho'
    if numero_ mes == 7
        return 'Julho'
    if numero_ mes == 8
        return 'Agosto'
    if numero_ mes == 9
        return 'Setembro'
    if numero_ mes == 10
        return 'Outubro'
    if numero_ mes == 11
        return 'Novembro'
    if numero_ mes == 12
        return 'Dezembro'
    else:
        return 'Invalido'
    
# exercicio_9

def data_valida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False
    if ano < 0:
        return False
    if dia<1 or dia>31:
        return False 
    if mes == 2:
        if dia > 29:
            return False 
        if dia == 29: 
            bissexto == (ano % 4) == 0
            return bissexto
    if dia == 31:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            return True
    return True

# exercicio_10

number = int(input('Digite um numero positivo de até 3 digitos'))

if number<0 or number>999:
        print('NÚMERO INVALIDO')
    
unidade = number % 10
dezena = (number//10)%10
centena = number//100

print('Centena:', centena)
print('Dezena:', dezena)
print('Unidade:', unidade)


