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
if 

