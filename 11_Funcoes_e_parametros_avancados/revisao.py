def validador_listas(lista, num):
    for linha in lista:
        if num in linha:
            return True 
    return False


# def validador_listas(tabela: list, numero: int) -> bool:
#   for linha in tabela:
#        for elemento in linha:
#           if elemento == numero:
#               return True
#   return False 


########################

def palindromo(palavra:str) -> bool:
    for i in 