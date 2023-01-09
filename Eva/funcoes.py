def registar_jogadores(op1, lista_jogadores):
    if op1 not in lista_jogadores:
        lista_jogadores.append(op1)
        return True
    else:
        
        return False

def remover_jogadores(lista_jogadores, op1, decorrer_jogo):
    
    if op1[1] in lista_jogadores:
        lista_jogadores.remove(op1[1])
        return True
    elif decorrer_jogo == 1 and op1[1] in lista_jogadores:
        return False
    else:
        return