def registar_jogadores(op1, lista_jogadores, dicionario_Jogos, decorrer_jogo):
    if op1.split(" ")[1] not in lista_jogadores:
        lista_jogadores.append(op1.split(" ")[1])

        # Organiza a 'lista_jogadores' alfabéticamente sempre que é adicionado um jogador novo
        lista_jogadores.sort()

        # Adiciona a 'dicionario_Jogos' as situações necessárias
        dicionario_Jogos.update({op1.split(" ")[1]: {'Jogos': 0, 'Vitorias': 0, 'em_Jogo': decorrer_jogo}})

        # Variavel 'chaves_organizadas' é as chaves de 'dicionario_Jogos' ordenadas alfabéticamente
        chaves_organizadas = sorted(dicionario_Jogos.keys())
        dicionario_organizado = {k: dicionario_Jogos[k] for k in chaves_organizadas}

        # Limpa o dicionário antigo e coloca o novo dicionário com as chaves ordenadas 
        dicionario_Jogos.clear()
        dicionario_Jogos.update(dicionario_organizado)

        return True

    else:
        return False

def remover_jogadores(lista_jogadores, op1, dicionario_Jogos):
    
    if op1.split(" ")[1] in lista_jogadores:
        lista_jogadores.remove(op1.split(" ")[1])

        dicionario_Jogos.pop(op1.split(" ")[1])

        chaves_organizadas = sorted(dicionario_Jogos.keys())
        dicionario_organizado = {k: dicionario_Jogos[k] for k in chaves_organizadas}

        dicionario_Jogos.clear()
        dicionario_Jogos.update(dicionario_organizado)
    
        return 1

    elif dicionario_Jogos[op1.split(" ")[1]]["em_Jogo"] == 1 and op1.split(" ")[1] in lista_jogadores:
        return 2
        
    else:
        return 3

def gravar_jogo(dicionario_Jogos, board, op1, decorrer_jogo, width):
    sorted_keys = sorted(dicionario_Jogos.keys())
    sorted_dictionary = {k: dicionario_Jogos[k] for k in sorted_keys}

    dicionario_Jogos.clear()
    dicionario_Jogos.update(sorted_dictionary)

    f = open(op1.split(" ")[1] + ".txt","a")

    # write file
    f.write("============= Informacao de jogos =============")
    f.write("\n")

    for jogador, jogos in dicionario_Jogos.items():
        f.write(str(jogador) + "\n" + str(jogos["Jogos"]) + " jogos\n" + str(jogos["Vitorias"]) + " vitorias \nEm jogo (1 - Sim | 0 - Nao) - " + str(jogos["em_Jogo"]) + "\n")
        f.write("\n")

    if decorrer_jogo == 1:
        f.write(" ".join([str(i + 1) for i in range(width)]))
        for row in board:
            f.write("|".join(row))

    # close file
    f.close()

    return True

def desistir_Jogo(
                    op1,                                # Para levar os nomes dos desistentes
                    decorrer_jogo,                      # Mudar o estado para 0
                    dicionario_Jogos,                   # Mudar o estado do 'decorrer_jogo'
                    nome_jogador1,                      # '' - Limpar
                    nome_jogador2,                      # '' - Limpar
                    width,                              # '' - Limpar
                    height,                             # '' - Limpar
                    sequenced_pieces,                   # '' - Limpar
                    special_pieces,                     # [] - Limpar
                    player_SpecialPiecesDictionary,     # {} - Limpar
                    num_special_pieces,                 # '' - Limpar
                    special_piece_size,                 # '' - Limpar
                    board,                              # [] - Limpar
                    player_X_special_pieces,            # [] - Limpar
                    player_O_special_pieces,            # [] - Limpar
                    jogador_atual,                      # '' - Limpar
                    column,                             # '' - Limpar
                    use_special_piece,                  # Default False
                    special_piece_index,                # Default None
                    orientation                         # '' - Limpar
                ):

                if len(op1.split(' ')) == 2:

                    keys = [player for player, game_info in dicionario_Jogos.items() if game_info["em_Jogo"] == 1]

                    # Visto que op1 só vai levar 1 jogador, ele terá de ir checkar qual é o outro que também está em jogo.
                    # Visto que só pode haver 2 players em jogo ao mesmo tempo we fine
                    if op1.split(' ')[1] in keys:
                        keys.remove(op1.split(' ')[1])

                    dicionario_Jogos[op1.split(' ')[1]]['em_Jogo'] = 0
                    dicionario_Jogos[keys[0]]['em_Jogo'] = 0

                    dicionario_Jogos[op1.split(' ')[1]]['Jogos'] += 1
                    dicionario_Jogos[keys[0]]['Jogos'] += 1

                    dicionario_Jogos[keys[0]]['Vitorias'] += 1

                    nome_jogador1 == ''
                    nome_jogador2 == ''

                    width == ''
                    height == ''
                    sequenced_pieces == ''
                    special_pieces.clear()
                    player_SpecialPiecesDictionary.clear()
                    num_special_pieces == ''
                    special_piece_size == ''
                    board.clear()
                    player_X_special_pieces.clear()
                    player_O_special_pieces.clear()
                    jogador_atual == ''
                    column == ''
                    use_special_piece == False
                    special_piece_index == None
                    orientation == ''

                    return 1
                
                elif len(op1.split(' ')) == 3:
                    dicionario_Jogos[op1.split(' ')[1]]['em_Jogo'] = decorrer_jogo
                    dicionario_Jogos[op1.split(' ')[2]]['em_Jogo'] = decorrer_jogo

                    dicionario_Jogos[op1.split(' ')[1]]['Jogos'] += 1
                    dicionario_Jogos[op1.split(' ')[2]]['Jogos'] += 1

                    nome_jogador1 == ''
                    nome_jogador2 == ''

                    width == ''
                    height == ''
                    sequenced_pieces == ''
                    special_pieces.clear()
                    player_SpecialPiecesDictionary.clear()
                    num_special_pieces == ''
                    special_piece_size == ''
                    board.clear()
                    player_X_special_pieces.clear()
                    player_O_special_pieces.clear()
                    jogador_atual == ''
                    column == ''
                    use_special_piece == False
                    special_piece_index == None
                    orientation == ''

                    return 1
                
                else:
                    return False
    

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

