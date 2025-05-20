def eh_primo(numero: int) -> bool:
    if numero <= 0:
        return 'Valor invalido'
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def test():
    assert not eh_primo(-1)
    assert not eh_primo(0)
    assert not eh_primo(1)
    assert eh_primo(2)
    assert eh_primo(3)
    assert not eh_primo(4)
    assert eh_primo(5)
