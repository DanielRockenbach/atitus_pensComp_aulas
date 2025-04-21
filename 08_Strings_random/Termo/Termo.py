import random

def dicionario(arquivo):
    with opeon(arquivo) as f:
        words = [line.strip()for line in f]
        return words

def chute_valido(chute, chutes)
    return chute in chutes

def avalia_chute(chute, palavra)
    str = ""

    for i in range(5):
        if chute[i] == palavra[i]
            str += "\033[32m" + chute[i]
        else:
            if chute[i] in [palavra]:
                str += "\033[33m" + chute[i]
                else:
                    str += "\033[0m" + chute[i]
    
    return str + "\033[0m"



def menu():
    print("Bem vindo, vamos jogar! ")
    print("Escolha seu modo de jogo: ")
    print("Digite 5 para: Palavras com 5 letras e 5 tentativas ")
    print("Digite 6 para: Palavras com 6 letras e 6 tentativas")
    print("Digite 7 para: Palavras com 7 letras e 7 tentativas")
    print("")
    
    segredo = random.choice(respostas)

    chutes = dicionario("")

    modo = int(input("Selecione o modo de jogo: "))
        if modo = 5:
            return
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if modo = 6:
            return
        if modo = 7:
            return
        if modo < 5 and modo > 7
            return 'Valor invalido, selecione '
