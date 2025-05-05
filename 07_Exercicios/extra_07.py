def fahrenheit_para_celsius(valor):
    f_para_c = (valor- 32)/1.8
    return f_para_c 

def celsius_para_fahrenheit(valor):
    c_para_f = (1.8* valor) + 32
    return c_para_f


assert fahrenheit_para_celsius(104) == 40
assert fahrenheit_para_celsius(-13) == -25

assert celsius_para_fahrenheit(40) == 104
assert celsius_para_fahrenheit(-25) == -13

assert celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30
