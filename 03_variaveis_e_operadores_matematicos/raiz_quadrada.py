def raiz_quadrada(valor):
    return valor ** (1 / 2)
    pass

def test():
    assert raiz_quadrada(9) == 3
    assert raiz_quadrada(16) == 4
    assert raiz_quadrada(25) == 5

print("Terminado com sucesso")
print(raiz_quadrada(9) == 3)
print(raiz_quadrada(16) == 4)
print(raiz_quadrada(25) == 5)
