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

def desistir_Jogo():
    return

################ JOGO ###################

def make_move_right(player, column, player_SpecialPiecesDictionary, height, width, board, use_special_piece, special_piece_index):
    column -= 1
    if use_special_piece:
        # Add the special piece
        special_piece_size = player_SpecialPiecesDictionary[player][special_piece_index]
        for i in range(column, column+special_piece_size):
            for j in range(height-1, -1, -1):
                if i < width and board[j][i] == ' ':
                    board[j][i] = player
                    break
        else:
            return True
    else:
        for i in range(height-1, -1, -1):
            if board[i][column] == ' ':
                board[i][column] = player
                return
        return True



def make_move_left(player, player_SpecialPiecesDictionary, height, board, column, use_special_piece, special_piece_index):
    column -= 1
    if use_special_piece:
        # Add the special piece
        special_piece_size = player_SpecialPiecesDictionary[player][special_piece_index]
        for i in range(column, column-special_piece_size, -1):
            for j in range(height-1, -1, -1):
                if i >= 0 and board[j][i] == ' ':
                    board[j][i] = player
                    break
        else:
            return True
    else:
        for i in range(height-1, -1, -1):
            if board[i][column] == ' ':
                board[i][column] = player
                return
        return True

def has_won(player, height, width, board, sequenced_pieces):
    # Check for win using special pieces
    for row in range(height):
        for col in range(width):
            # Check if the current position is a special piece
            if board[row][col] == player:
                # Check if the special piece is long enough to win
                special_piece_size = 0
                while col+special_piece_size < width and board[row][col+special_piece_size] == player:
                    special_piece_size += 1
                if special_piece_size >= sequenced_pieces:
                    return True
                
                # Check if the special piece is tall enough to win
                special_piece_size = 0
                while row+special_piece_size < height and board[row+special_piece_size][col] == player:
                    special_piece_size += 1
                if special_piece_size >= sequenced_pieces:
                    return True
    
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


