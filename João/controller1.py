def colocar_peca(n,x,y):
    for n in range(1,x):
        for n in range(1,y):
            pass
# def colocar_peca(n,x,y,a,p):
#     for n in range(1,x):
#         for n in range(1,y):
#            if  
#              a.append()
def adicionar_jogador(lista, jogador):
    if jogador not in lista:
        lista.append(jogador)
        return True

def eliminar_jogador(lista, jogador):
    if jogador in lista:
        lista.remove(jogador)
        return True

def registar_Jogadores(nome_jogador, lista_jogadores):
    if nome_jogador in lista_jogadores:
        x = ("Jogador existente.")
        return x
    else:
        lista_jogadores.append(nome_jogador)
        x = ("Jogador registado com sucesso.")
        return x

def remover_Jogadores(lista_Jogadores, nome_apagarJogador, decorrer_Jogo):
    if nome_apagarJogador in lista_Jogadores:
        lista_Jogadores.remove(nome_apagarJogador)
        x = ("Jogador removido com sucesso.")
        return x
    elif decorrer_Jogo == 1 and nome_apagarJogador in lista_Jogadores:
        x = ("Jogador participa no jogo em curso.")
        return x
    else:
        x = ("Jogador não existente.")
        return x

def movimento_Jogada(jogada, coluna, tabuleiro):
    coluna -= 1
    for i in range(5, -1, -1):
        if tabuleiro[i][coluna] == ' ':
            tabuleiro[i][coluna] = jogada
            return
    x = ("A coluna encontra-se completa, escolhe outra coluna.")        
    return x

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

def LJ(lista,z):
    for i in range(0,z):
        return lista
def detalhes_jogo(jogador_1,jogador_2,comprimento_Grelha,altura_Grelha,tamanho_Sequencia):
    x  =(f'''Para vencer é necessario o {jogador_1} ou o {jogador_2} 
        numa tabela de {comprimento_Grelha} comprimento e {altura_Grelha} altura         DENTRO E FORA DO IJ MAS ESTE É O DE DENTRO          
        colocar {tamanho_Sequencia} peças em linha horizontal,vertical ou diagonal.
        ''')
    return x        
        
