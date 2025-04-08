def desenha_losango(altura):
    if altura % 2 == 0:
        altura = altura + 1
    meio = altura // 2
    for linha in range(altura):
        if linha <= meio
            spaces =  meio - linha
            star = linha * 2 + 1
    else: 
        spaces = linha - meio
        star = altura - (linha - meio)*2
    print(',' * spaces + '#' * star)
    
    


altura = int(input("Digite um valor ímpar para a altura do losango: "))
desenha_losango(altura)


#altura = int(input("Digite um valor ímpar para a altura do losango: "))
# Se a altura for par, incrementa em 1 para garantir uma linha central
#if altura % 2 == 0:
 #   altura = altura + 1
  #  print("O valor digitado era par, usaremos", altura, "no lugar")

#meio = altura // 2  # Linha do meio do losango (considere que a contagem inicia em 0)
#for linha_atual in range(altura):  # Itera de 0 até altura
    # Desenhando a parte superior do losango (primeira linha até meio, incluindo o meio)
#    if linha_atual <= meio:
#        num_espacos = meio - linha_atual
#       num_star = linha_atual * 2 + 1
#    else:  # Desenhando parte inferior do losango
#        num_espacos = linha_atual - meio
#        num_star = altura - (linha_atual - meio) * 2
#    print("." * num_espacos + "#" * num_star)