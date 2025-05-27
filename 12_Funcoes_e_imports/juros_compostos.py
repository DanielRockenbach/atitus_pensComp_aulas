def calcular_juros_compostos(valor: int, taxa:int, tempo: int) -> int|None :
    if valor < 0:
        return None
    if tempo < 0:
        return None
    return valor * ((1 + taxa)** tempo)
        
        



def calcular_juros_compostos_recursivo(principal, taxa, tempo):
    pass


assert calcular_juros_compostos(1000, 0.05, 5) == 1276.2815625000003
assert calcular_juros_compostos(1000, 0.05, 10) == 1628.894626777442
assert calcular_juros_compostos(1000, 0.05, 0) == 1000

assert calcular_juros_compostos_recursivo(1000, 0.05, 5) == 1276.2815625000003
assert calcular_juros_compostos_recursivo(1000, 0.05, 10) == 1628.894626777442
assert calcular_juros_compostos_recursivo(1000, 0.05, 0) == 1000
