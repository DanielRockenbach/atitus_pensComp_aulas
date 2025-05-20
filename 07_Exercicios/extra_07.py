<<<<<<< HEAD
def fahrenheit_para_celsius(valor): #Extra 07  
    return (valor - 32) / 1.8
=======
def fahrenheit_para_celsius(valor):
    f_para_c = (valor- 32)/1.8
    return f_para_c 
>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2

<<<<<<< HEAD


=======
>>>>>>> 043c61666b61699165f87a4d2a78813f467719c2
def celsius_para_fahrenheit(valor):
    c_para_f = (1.8* valor) + 32
    return c_para_f

def test():
    assert fahrenheit_para_celsius(104) == 40
    assert fahrenheit_para_celsius(-13) == -25

    assert celsius_para_fahrenheit(40) == 104
    assert celsius_para_fahrenheit(-25) == -13

    assert celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30
