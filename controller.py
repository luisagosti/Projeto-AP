def colocar_peca(n,x,y):
    for n in range(1,x):
        for n in range(1,y):
            pass

def registar_jogadores(nome_jogador, lista_jogadores):
    if nome_jogador in lista_jogadores:
        return False
    else:
        lista_jogadores.append(nome_jogador)
        return True

def remover_jogadores(lista_jogadores, nome_apagar_jogador, decorrer_jogo):
    if nome_apagar_jogador in lista_jogadores:
        lista_jogadores.remove(nome_apagar_jogador)
        return True
    elif decorrer_jogo == 1 and nome_apagar_jogador in lista_jogadores:
        return False
    else:
        return

def movimento_jogada(jogada, coluna, tabuleiro):
    coluna -= 1
    for i in range(5, -1, -1):
        if tabuleiro[i][coluna] == ' ':
            tabuleiro[i][coluna] = jogada
            return       
    return True

def verificar_vitoria(jogada, tabuleiro, coluna):
    # Verifica vitória horizontal
    for linha in tabuleiro:
        if linha.count(jogada) == 4:
            return True
    # Verifica vitória vertical
    for coluna in range(7):
        if tabuleiro[0][coluna] == jogada and tabuleiro[1][coluna] == jogada and tabuleiro[2][coluna] == jogada and tabuleiro[3][coluna] == jogada:
            return True
    # Verifica vitória diagonal
    for linha in range(3):
        for coluna in range(4):
            if tabuleiro[linha][coluna] == jogada and tabuleiro[linha+1][coluna+1] == jogada and tabuleiro[linha+2][coluna+2] == jogada and tabuleiro[linha+3][coluna+3] == jogada:
                return True
    for linha in range(3):
        for coluna in range(4):
            if tabuleiro[linha+3][coluna] == jogada and tabuleiro[linha+2][coluna+1] == jogada and tabuleiro[linha+1][coluna+2] == jogada and tabuleiro[linha][coluna+3] == jogada:
                return True
    return False

def listar_jogadores(lista,z):
    for i in range(0,z):
        return lista
     
        