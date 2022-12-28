def registar_Jogadores(nome_Jogador, lista_Jogadores):
    if nome_Jogador in lista_Jogadores:
        return "Jogador existente."
    else:
        lista_Jogadores.append(nome_Jogador)
        return "Jogador registado com sucesso."

def remover_Jogadores(lista_Jogadores, nome_apagarJogador, decorrer_Jogo):
    if nome_apagarJogador in lista_Jogadores:
        lista_Jogadores.remove(nome_apagarJogador)
        return "Jogador removido com sucesso."
    elif decorrer_Jogo == 1 and nome_apagarJogador in lista_Jogadores:
        return "Jogador participa no jogo em curso."
    else:
        return "Jogador não existente."

def movimento_Jogada(jogada, coluna, tabuleiro):
    coluna -= 1
    for i in range(5, -1, -1):
        if tabuleiro[i][coluna] == ' ':
            tabuleiro[i][coluna] = jogada
            return
    return "A coluna encontra-se completa, escolhe outra coluna."

def verificar_Vitoria(jogada, tabuleiro, coluna):
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