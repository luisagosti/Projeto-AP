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

def print_board(width, board):
    # Print the column numbers
    print(' '.join([str(i+1) for i in range(width)]))
    for row in board:
        print('|'.join(row))

def make_move(player, column, height, board):
    column -= 1
    for i in range(height-1, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = player
            return
    print("A coluna encontra-se completa, escolhe outra coluna.")

def has_won(player, board, width, height, sequenced_pieces):
    # Check for horizontal win
    for row in board:
        for i in range(width - sequenced_pieces + 1):
            if all(row[i+j] == player for j in range(sequenced_pieces)):
                return True
    
    # Check for vertical win
    for col in range(width):
        if all(board[row][col] == player for row in range(height)):
            return True
    
    # Check for diagonal win (top-left to bottom-right)
    for row in range(height - sequenced_pieces + 1):
        for col in range(width - sequenced_pieces + 1):
            if all(board[row+i][col+i] == player for i in range(sequenced_pieces)):
                return True
    
    # Check for diagonal win (top-right to bottom-left)
    for row in range(height - sequenced_pieces + 1):
        for col in range(width - 1, sequenced_pieces - 2, -1):
            if all(board[row+i][col-i] == player for i in range(sequenced_pieces)):
                return True
    
    # Check for win in all other directions
    for row in range(height - sequenced_pieces + 1):
        for col in range(width):
            # Check for win in top-bottom direction
            if all(board[row+i][col] == player for i in range(sequenced_pieces)):
                return True
            # Check for win in left-right direction
            if all(board[row][col+i] == player for i in range(sequenced_pieces)):
                return True
    return False

