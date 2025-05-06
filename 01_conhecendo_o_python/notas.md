pessoas = int(input("Quantas pessoas?"))

soma = sum(int(input("Idade: ")) for _ in range(pessoas))

print("Média:" , soma / pessoas)