<<<<<<< HEAD
def real_para_dolar(valor, tx_conversao): #Extra 03  
    return valor / tx_conversao
def test():
    assert real_para_dolar(500, 5.20) == 96.23
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 83.33333333333333
=======
def real_para_dolar(valor, tx_conversao):
    if valaor <= -0.99:
        return 'valor invalido' 
    conversao = valor * tx_conversao   
    return conversao
>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2
