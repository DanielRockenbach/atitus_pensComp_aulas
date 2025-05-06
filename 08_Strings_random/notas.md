# Daniel, Julia e Henrique

ano_nascimento = int(input('Digite o ano de nascimento: '))
aposentadoria =  int(input('Digite  com quantos anos você deseja se aposentar: '))
expectativa_vida = int(input('Digite a idade na qual você espera viver: '))
ANO_ATUAL = 2025
idade = ANO_ATUAL - ano_nascimento
if expectativa_vida < idade:
    print ('Valor inválido')
patrimonio = int(input('Digite seu patrimonio atual: '))
if patrimonio < 0:
    print('Valor invalido')
tx_anual = int(input('Digite sua taxa anual de crescimento de patrimônio: '))
if tx_anual < 0:
    print('Valor invalido')
valor_aporte = int(input('Digite o valor de aporte mensal: '))
custo_mensal = int(input('Digite o valor do custo mensal: '))


ANO_ATUAL = 2025
idade = ANO_ATUAL - ano_nascimento
ano_aposentado = ano_nascimento + aposentadoria
a_faltas = aposentadoria - idade
taxa_mensal = 1.007974


for mes in range(aposentadoria * 12):
    patrimonio = (patrimonio * taxa_mensal) + valor_aporte
    


gasto = expectativa_vida - aposentadoria

for mes in range(gasto - (custo_mensal * 12)):
    patrimonio = (patrimonio * taxa_mensal) - gasto

print (f"Seu acumulo de herança é R$ {patrimonio}")