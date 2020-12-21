quantidade_vagoes = input()
while quantidade_vagoes != '0':
     
    vagoes = input()
    saida = input()

    letras = vagoes.split(' ')
    estacao = []
    string_final = []
    insere_remove = ""

    for vagao_saida in saida.split(' '):

        if vagao_saida in estacao:
            
            if vagao_saida == estacao[len(estacao)-1]:
                insere_remove += "R"
                string_final.append(estacao.pop())
                continue
            else:
                print(insere_remove + " Impossible")  
        elif vagao_saida in letras:
            while vagao_saida in letras:
                estacao.append(letras.pop(0))
                insere_remove += "I"
        else:
            print(insere_remove + " Impossible")  

        
        if len(estacao) > 0:
            if estacao[len(estacao) - 1] == vagao_saida:
                string_final.append(estacao.pop())
                insere_remove += "R"
            else:
                print(insere_remove + " Impossible")


   

    # while(letras.pop())
    # print(a)
    quantidade_vagoes = input()
