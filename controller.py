def registar_jogadores(nome_jogador, lista_jogadores):
    x = nome_jogador.upper()
    if x in lista_jogadores:
        return False
    else:
        lista_jogadores.append(x)
        return True

def remover_jogadores(lista_jogadores, nome_apagar_jogador, decorrer_jogo):
    x = nome_apagar_jogador.upper()
    if x in lista_jogadores:
        lista_jogadores.remove(x)
        return True
    elif decorrer_jogo == 1 and x in lista_jogadores:
        return False
    else:
        return

def movimento_jogada(jogada, coluna, tabuleiro, altura_grelha):
    coluna -= 1
    for i in range(altura_grelha - 1, -1, -1):
        if tabuleiro[i][coluna] == ' ':
            tabuleiro[i][coluna] = jogada
            return tabuleiro     
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

def gravar_jogo(lista_jogadores, decorrer_jogo, tabuleiro, temp_var):
    with open('resultados.txt', 'w') as f:

        f.write("Lista Jogadores: \n")
        for i in len(lista_jogadores):
            f.write(str(i + 1) + "º Jogador - " + lista_jogadores[i])
            f.write('\n')

        if decorrer_jogo == 1:
            f.write("Jogo a decorrer atualmente: \n")
            f.write(temp_var)
            f.write('\n')
            for row in tabuleiro:
                f.write('|'.join(row))
                f.write('\n')
        else:
            f.write("Não se encontra nenhum jogo a decorrer.")
            f.write('\n')

        return True

     
        