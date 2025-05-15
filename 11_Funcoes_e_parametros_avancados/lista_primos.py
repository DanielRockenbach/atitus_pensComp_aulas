def eh_primo(numero: int) -> bool:
    if numero <= 0:
        return 'Valor invalido'
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def lista_primos(num:int) -> list:
    lista_primos = []
    for j in range(num + 1):
        if eh_primo(j):
            lista_primos.append(j)
    return lista_primos

def test():
    assert lista_primos(10) == [2, 3, 5, 7]
    assert lista_primos(13) == [2, 3, 5, 7, 11, 13]
    assert lista_primos(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print(lista_primos(100))