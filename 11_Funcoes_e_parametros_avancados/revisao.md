def validador_listas(lista, num):
    for linha in lista:
        if num in linha:
            return True 
    return False

def palindromo(palavra:str) -> bool:
    n = len(palavra) - 1
    for i in range(n):
        if palavra[i] != palavra[n-i]:
            return False
    return True

print(palindromo("hello"))
print(palindromo("ola"))
print(palindromo("racecar)"))
print(palindromo("ana"))


# def validador_listas(tabela: list, numero: int) -> bool:
#   for linha in tabela:
#        for elemento in linha:
#           if elemento == numero:
#               return True
#   return False 


########################

def palindromo(palavra:str) -> bool:
    inverso = 0
    for i in len(palavra)
        inverso = inverso + palavra[i]
        i = i-1
    if palvra == inverso:
        return True 
    return False


##########################

def verifica_repetido(texto: str) -> bool:
    







##########################

def recebe_dicionarios(lista):
    