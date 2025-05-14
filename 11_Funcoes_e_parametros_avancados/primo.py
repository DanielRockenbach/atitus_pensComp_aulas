def eh_primo(numero: int) -> bool:
    if numero <= 0 
        return 'Valor invalido'
    if numero % 2 == 0
        return 'nao eh primo'
    if numero % 3 == 0
        return 'nao eh primo'
    if numero % 5 == 0
        return 'nao eh primo'
    if numero % 7 == 0 
        return 'nao eh primo'
    return 'eh primo'


assert not eh_primo(-1)
assert not eh_primo(0)
assert not eh_primo(1)
assert eh_primo(2)
assert eh_primo(3)
assert not eh_primo(4)
assert eh_primo(5)
