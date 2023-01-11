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

# def movimento_jogada(jogada, coluna, tabuleiro, altura_grelha):
#     coluna -= 1
#     for i in range(altura_grelha - 1, -1, -1):
#         if tabuleiro[i][coluna] == ' ':
#             tabuleiro[i][coluna] = jogada
#             return tabuleiro     
#     return True

# def verificar_vitoria(jogada, tabuleiro, coluna):
#     # Verifica vitória horizontal
#     for linha in tabuleiro:
#         if linha.count(jogada) == 4:
#             return True
#     # Verifica vitória vertical
#     for coluna in range(7):
#         if tabuleiro[0][coluna] == jogada and tabuleiro[1][coluna] == jogada and tabuleiro[2][coluna] == jogada and tabuleiro[3][coluna] == jogada:
#             return True
#     # Verifica vitória diagonal
#     for linha in range(3):
#         for coluna in range(4):
#             if tabuleiro[linha][coluna] == jogada and tabuleiro[linha+1][coluna+1] == jogada and tabuleiro[linha+2][coluna+2] == jogada and tabuleiro[linha+3][coluna+3] == jogada:
#                 return True
#     for linha in range(3):
#         for coluna in range(4):
#             if tabuleiro[linha+3][coluna] == jogada and tabuleiro[linha+2][coluna+1] == jogada and tabuleiro[linha+1][coluna+2] == jogada and tabuleiro[linha][coluna+3] == jogada:
#                 return True
#     return False

def listar_jogadores(lista,z):
    for i in range(0,z):
        return lista

def gravar_jogo(lista_jogadores, decorrer_jogo, board, temp_var):
    with open('resultados.txt', 'w') as f:

        f.write("Lista Jogadores: \n")
        for i in len(lista_jogadores):
            f.write(str(i + 1) + "º Jogador - " + lista_jogadores[i])
            f.write('\n')

        if decorrer_jogo == 1:
            f.write("Jogo a decorrer atualmente: \n")
            f.write(temp_var)
            f.write('\n')
            for row in board:
                f.write('|'.join(row))
                f.write('\n')
        else:
            f.write("Não se encontra nenhum jogo a decorrer.")
            f.write('\n')

        return True

################ Testes ###################

def print_tabuleiro(comprimento_grelha, tabuleiro):
    # Printar o numero de colunas
    print(' '.join([str(i+1) for i in range(comprimento_grelha)]))
    for row in tabuleiro:
        print('|'.join(row))

def jogada(jogador, coluna, altura_grelha, tabuleiro):
    coluna -= 1
    for i in range(altura_grelha-1, -1, -1):
        if tabuleiro[i][coluna] == ' ':
            tabuleiro[i][coluna] = jogador
            return
    print("A coluna encontra-se completa, escolhe outra coluna.")

def ganhar(jogador, tabuleiro, comprimento_grelha, altura_grelha, tamanho_sequencia):
    # Verificar vitória na horizontal
    for row in tabuleiro:
        for i in range(comprimento_grelha - tamanho_sequencia + 1):
            if all(row[i+j] == jogador for j in range(tamanho_sequencia)):
                return True
    
    # Verificar vitória na vertical
    for col in range(comprimento_grelha):
        if all(tabuleiro[row][col] == jogador for row in range(altura_grelha)):
            return True
    
    # Verificar vitória na diagonal (do topo esquerdo para o fundo direito)
    for row in range(altura_grelha - tamanho_sequencia + 1):
        for col in range(comprimento_grelha - tamanho_sequencia + 1):
            if all(tabuleiro[row+i][col+i] == jogador for i in range(tamanho_sequencia)):
                return True
    
    # Verificar vitória na diagonal (do topo direito para o fundo esquerdo)
    for row in range(altura_grelha - tamanho_sequencia + 1):
        for col in range(comprimento_grelha - 1, tamanho_sequencia - 2, -1):
            if all(tabuleiro[row+i][col-i] == jogador for i in range(tamanho_sequencia)):
                return True
    
    # Verificar vitória em todas as direções
    for row in range(altura_grelha - tamanho_sequencia + 1):
        for col in range(comprimento_grelha):
            # Verificar vitória na direção topo-fundo
            if all(tabuleiro[row+i][col] == jogador for i in range(tamanho_sequencia)):
                return True
            # Verificar vitória na direção esquerda-direita
            if all(tabuleiro[row][col+i] == jogador for i in range(tamanho_sequencia)):
                return True
    return False

