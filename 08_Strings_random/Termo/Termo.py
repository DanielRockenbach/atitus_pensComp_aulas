import random

def dicionario(arquivo):
    with open(arquivo) as f:
        palavra = [line.strip() for line in f]
        return palavras

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
    print("Digite 6 para: Palavras com 6 letras e 6 tentativas ")
    print("Digite 7 para: Palavras com 7 letras e 7 tentativas ")
    print("")
    
def termo(chutes, resposta)
    segredo = random.choice(respostas)

    tentativas = 1
    max_tentativas = 5
    
    while tentativas <= max_tentativas:
        chute = input("Enter guess #" + str(tentativas) + ": ").lower()
        if not chute_valido(chute, chutes):
                print("Tentativa invalida, digite uma palavra em portugues com 5 letras.")
                continue 
        if chute == segredo:
            print("Parabéns! Você acertou qual era a palavra secreta: ", segredo)
            break
        
        tentativas += 1
        feedback = avalia_chute(chute, segredo)
        print(feedback)

    if tentativas > max_tentativas:
        Print("Jogo encerrado, suas tentaivas acabaram. A palavra secreta era: ", segredo)

    #chutes = dicionario("Dicionario_5.txt")
    #respostas = dicionario("resposta_5.txt")
    
    #chutes = dicionario("Dicionario_6.txt")
    #respostas = dicionario("respostas_6.txt")
    
    #chutes = dicionario("Dicionario_7.txt")
    #respostas = dicionario("respostas_7.txt")

    modo = int(input("Selecione o modo de jogo: "))
        if modo = 5:
            chutes = dicionario("Dicionario_5.txt")
            respostas = dicionario("resposta_5.txt")
            return termo
        elif modo = 6:
            chutes = dicionario("Dicionario_6.txt")
            respostas = dicionario("respostas_6.txt")
            return termo
        elif modo = 7:
            chutes = dicionario("Dicionario_7.txt")
            respostas = dicionario("respostas_7.txt")
            return termo
       else:
            'Valor invalido'