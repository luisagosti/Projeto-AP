def registar_jogadores(op1, lista_jogadores,x):
    if op1 not in lista_jogadores:
        lista_jogadores.append(op1)
        p = ((op1),'Vitoria')               #O p e o o sao variaveis que iram armazenar a string vitoria e a string jogos_jogados
        o = ((op1),'jogos_jogados')
        y = {(p):0,(o):0}       # Dicionario y atribui valores a p e o 
        x.update(y)             #Dicionario final de modo a não repetir nomes de variaveis
        print(x)
        return True

    else:
        return False

def remover_jogadores(lista_jogadores, op1, decorrer_jogo,x):
    
    if op1[1] in lista_jogadores:
        lista_jogadores.remove(op1[1])
    
        return True

    elif decorrer_jogo == 1 and op1[1] in lista_jogadores:
        return False
        
    else:
        return

def desistir_jogo(op1, lista_jogadores, nome_jogador1, nome_jogador2):
    if op1[1] not in lista_jogadores:
        return 1                                                                            #Jogador um não registado
    if op1[2] not in lista_jogadores:
        return 2                                                                            #Jogador dois não registado
    elif op1[1] != nome_jogador1 or op1[1] != nome_jogador2 and op1[1] in lista_jogadores :
        return 3                                                                            #Jogador não participa do jogo em curso
    elif op1[2] != nome_jogador1 or op1[2] != nome_jogador2 and op1[2] in lista_jogadores :
        return 3                                                                            #Jogador não participa do jogo em curso
    elif op1[1] == nome_jogador1 and op1[2] == nome_jogador2:
        return 4                                                                            #fim de jogo, ninguem vence
    elif op1[1] == nome_jogador2 and op1[2] == nome_jogador1:
        return 4                                                                            #fim de jogo, ninguem vence
    elif op1[1] == nome_jogador1:
        return 5                                                                            #fim de jogo, jogador 2 vence
    elif op1[1] == nome_jogador2:
        return 6                                                                            #fim de jogo, jogador 1 vence 