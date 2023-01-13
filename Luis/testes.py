# # Get board width and height from user
# width = int(input("Indica o comprimento do tabuleiro: "))
# height = int(input("Indica a altura do tabuleiro: "))

# # Get the number of sequenced pieces needed to win
# sequenced_pieces = int(input("Indica o numero de peças em sequência necessárias para ganhar: "))

# # Create a list to store the special pieces
# special_pieces = []

# # Create a dictionary to save the number of special pieces within the player name
# player_SpecialPiecesDictionary = {}

# # Get the number and size of special pieces from the user
# num_special_pieces = int(input("Indica o numero de peças especiais: "))
# for i in range(num_special_pieces):
#     special_piece_size = int(input("Indica o tamanho da {} peça especial: ".format(i+1)))
#     special_pieces.append(special_piece_size)

# # Generate board with the specified width and height
# board = [[' ' for _ in range(width)] for _ in range(height)]

# def print_board():
#     # Print the column numbers
#     print(' '.join([str(i+1) for i in range(width)]))
#     for row in board:
#         print('|'.join(row))

# def make_move_right(player, column, use_special_piece=False, special_piece_index=None):
#     column -= 1
#     if use_special_piece:
#         # Add the special piece
#         special_piece_size = player_SpecialPiecesDictionary[player][special_piece_index]
#         for i in range(column, column+special_piece_size):
#             for j in range(height-1, -1, -1):
#                 if i < width and board[j][i] == ' ':
#                     board[j][i] = player
#                     break
#         else:
#             print("A coluna encontra-se completa, escolhe outra coluna.")
#             return
#     else:
#         for i in range(height-1, -1, -1):
#             if board[i][column] == ' ':
#                 board[i][column] = player
#                 return
#         print("A coluna encontra-se completa, escolhe outra coluna.")

# def make_move_left(player, column, use_special_piece=False, special_piece_index=None):
#     column -= 1
#     if use_special_piece:
#         # Add the special piece
#         special_piece_size = player_SpecialPiecesDictionary[player][special_piece_index]
#         for i in range(column, column-special_piece_size, -1):
#             for j in range(height-1, -1, -1):
#                 if i >= 0 and board[j][i] == ' ':
#                     board[j][i] = player
#                     break
#         else:
#             print("A coluna encontra-se completa, escolhe outra coluna.")
#             return
#     else:
#         for i in range(height-1, -1, -1):
#             if board[i][column] == ' ':
#                 board[i][column] = player
#                 return
#         print("A coluna encontra-se completa, escolhe outra coluna.")

# def has_won(player):
#     # Check for win using special pieces
#     for row in range(height):
#         for col in range(width):
#             # Check if the current position is a special piece
#             if board[row][col] == player:
#                 # Check if the special piece is long enough to win
#                 special_piece_size = 0
#                 while col+special_piece_size < width and board[row][col+special_piece_size] == player:
#                     special_piece_size += 1
#                 if special_piece_size >= sequenced_pieces:
#                     return True

#                 # Check if the special piece is tall enough to win
#                 special_piece_size = 0
#                 while row+special_piece_size < height and board[row+special_piece_size][col] == player:
#                     special_piece_size += 1
#                 if special_piece_size >= sequenced_pieces:
#                     return True

#     # Check for horizontal win
#     for row in board:
#         for i in range(width - sequenced_pieces + 1):
#             if all(row[i+j] == player for j in range(sequenced_pieces)):
#                 return True

#     # Check for vertical win
#     for col in range(width):
#         if all(board[row][col] == player for row in range(height)):
#             return True

#     # Check for diagonal win (top-left to bottom-right)
#     for row in range(height - sequenced_pieces + 1):
#         for col in range(width - sequenced_pieces + 1):
#             if all(board[row+i][col+i] == player for i in range(sequenced_pieces)):
#                 return True

#     # Check for diagonal win (top-right to bottom-left)
#     for row in range(height - sequenced_pieces + 1):
#         for col in range(width - 1, sequenced_pieces - 2, -1):
#             if all(board[row+i][col-i] == player for i in range(sequenced_pieces)):
#                 return True

#     # Check for win in all other directions
#     for row in range(height - sequenced_pieces + 1):
#         for col in range(width):
#             # Check for win in top-bottom direction
#             if all(board[row+i][col] == player for i in range(sequenced_pieces)):
#                 return True
#             # Check for win in left-right direction
#             if all(board[row][col+i] == player for i in range(sequenced_pieces)):
#                 return True

#     return False


# # Initialize separate lists for each player's special pieces
# player_X_special_pieces = special_pieces.copy()
# player_O_special_pieces = special_pieces.copy()

# # Update player_SpecialPiecesDictionary with the separate lists
# player_SpecialPiecesDictionary.update({"X": player_X_special_pieces, "O": player_O_special_pieces})

# def main():
#     player = 'X'
#     while True:
#         print("player_SpecialPiecesDictionary: " + str(player_SpecialPiecesDictionary))
#         print_board()
#         column = int(input(f"{player}, escolhe uma coluna ou '0' para jogar uma peça especial: "))
#         use_special_piece = False
#         special_piece_index = None

#         if column == 0:
#             if len(player_SpecialPiecesDictionary[player]) > 0:
#                 print("Escolhe qual peça especial queres usar:")
#                 for i, special_piece in enumerate(player_SpecialPiecesDictionary[player]):
#                     print("{}: {} sequencias".format(i+1, special_piece))
#                 special_piece_index = int(input("Peça especial: ")) - 1
#                 use_special_piece = True
#                 orientation = input("Em que sentido queres jogar a peça especial (E ou D): ")
#                 column = int(input("Em que coluna queres jogar a peça especial: "))

#             else:
#                 print("Não existem peças especiais.")
#                 continue
#         elif column < 0 or column > width:
#             print("Coluna inválida, escolhe outra coluna.")
#             continue

#         if use_special_piece == True:
#             if orientation == "E":
#                     make_move_left(player, column, use_special_piece=use_special_piece, special_piece_index=special_piece_index)

#             elif orientation == "D":
#                 make_move_right(player, column, use_special_piece=use_special_piece, special_piece_index=special_piece_index)

#             else:
#                 print("Orientação inválida, escolhe outra coluna.")
#                 continue
#         else:
#             make_move_right(player, column, use_special_piece=use_special_piece, special_piece_index=special_piece_index)

#         if use_special_piece:
#             special_piece = player_SpecialPiecesDictionary[player][special_piece_index]
#             player_SpecialPiecesDictionary[player].remove(special_piece)
#         if has_won(player):
#             print_board()
#             print(f"{player} Venceu!")
#             break
#         player = 'O' if player == 'X' else 'X'

# main()

# decorrer_jogo = 0

# op1 = 'RJ Pedro'

dicionario_Jogos = {
    "Pedro": {"Jogos": 0, "Vitorias": 0, "em_Jogo": 1},
    "João": {"Jogos": 1, "Vitorias": 1, "em_Jogo": 1},
    "Ana": {"Jogos": 2, "Vitorias": 2, "em_Jogo": 0},
}

# sorted_keys = sorted(dicionario_Jogos.keys())
# sorted_dictionary = {k: dicionario_Jogos[k] for k in sorted_keys}

# dicionario_Jogos.clear()
# dicionario_Jogos.update(sorted_dictionary)

# f = open("dict.txt","a")

# # write file
# f.write("============= Informacao de jogos =============")
# f.write("\n")

# for jogador, jogos in dicionario_Jogos.items():
#     f.write(str(jogador) + "\n" + str(jogos["Jogos"]) + " jogos\n" + str(jogos["Vitorias"]) + " vitorias \nEm jogo (1 - Sim | 0 - Nao) - " + str(jogos["em_Jogo"]) + "\n")
#     f.write("\n")

# # close file
# f.close()


try:
    f = open('dict.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

except FileNotFoundError:
    print('File does not exist')

print(
    """
RJ + Nome - Registar jogador
EJ + Nome - Remover jogador
LJ - Listar jogadores
IJ + 2 Nomes - Iniciar jogo
DJ - Detalhes do jogo
D + 1/2 Nomes - Desistir
CP + Nome + TamanhoPeça + Posição + (Sentido) - Colocar peça
V - Visualizar resultado
G - Gravar
L - Ler
X - Sair """
)
op1 = input("Digite uma opção: ")  # Opção 1





# Visto que op1 só vai levar 1 jogador, ele terá de ir checkar qual é o outro que também está em jogo.
# Visto que só pode haver 2 players em jogo ao mesmo tempo we fine
# print(keys)

# if op1.split(' ')[1] in keyss:
#     keys.remove(op1.split(' ')[1])

# print(keys)

# sorted_keys = sorted(dicionario_Jogos.keys())
# sorted_dictionary = {k: dicionario_Jogos[k] for k in sorted_keys}

# dicionario_Jogos.clear()
# dicionario_Jogos.update(sorted_dictionary)

# for jogador, jogos in dicionario_Jogos.items():
#     print(str(jogador) + " - " + str(jogos["Jogos"]) + " jogos,", str(jogos["Vitorias"]) + " vitórias.")




# dicionario_Jogos.update({"Katya": {'Jogos': 0, 'Vitorias': 0, 'em_Jogo': decorrer_jogo}})

# sorted_keys = sorted(dicionario_Jogos.keys())
# sorted_dictionary = {k: dicionario_Jogos[k] for k in sorted_keys}

# dicionario_Jogos.clear()
# dicionario_Jogos.update(sorted_dictionary)

# print(dicionario_Jogos)

# dicionario_Jogos.pop("João")

# sorted_keys = sorted(dicionario_Jogos.keys())
# sorted_dictionary = {k: dicionario_Jogos[k] for k in sorted_keys}

# dicionario_Jogos.clear()
# dicionario_Jogos.update(sorted_dictionary)

# print(dicionario_Jogos)



# print('''
#     RJ + Nome - Registar jogador
#     EJ + Nome - Remover jogador
#     LJ - Listar jogadores
#     IJ + 2 Nomes - Iniciar jogo
#     DJ - Detalhes do jogo
#     D + 1/2 Nomes - Desistir
#     CP + Nome + TamanhoPeça + Posição + (Sentido) - Colocar peça
#     V - Visualizar resultado
#     G - Gravar
#     L - Ler
#     X - Sair ''')
# op1 = input("Digite uma opção: ")  # Opção 1

# # Enquanto a "Opção 1" não igualar nenhuma das opções do array, o programa irá continuar a perguntar por uma opção.
# # Ele passa quando a "Opção 1" for equivalente a alguma das opções dentro do array
# while (op1.split(" ")[0].upper() not in ["RJ", "EJ", "LJ", "IJ", "DJ", "D", "CP", "V", "G", "L", "X"]
#     or op1.split(" ")[0].upper() in ["V", "G", "L", "X"] and len(op1) > 1
#     or len(op1.split(" ")) > 5
#     or op1.split(" ")[0].upper() in ["RJ", "EJ"] and len(op1.split(" ")) != 2
#     or op1.split(" ")[0].upper() in ["LJ", "DJ", "CP"] and len(op1.split(" ")) >= 2
#     or op1.split(" ")[0].upper() in ["CP"] and len(op1.split(" ")) > 5
#     or op1.split(" ")[0].upper() in ["IJ"] and len(op1.split(" ")) != 3
#     or op1.split(" ")[0].upper() in ["D"] and (len(op1.split(" ")) > 3 or len(op1.split(" ")) < 2)):
#     # os.system("cls")

#     print("Instrução inválida.")
#     print('''
#     RJ + Nome - Registar jogador
#     EJ + Nome - Remover jogador
#     LJ - Listar jogadores
#     IJ + 2 Nomes - Iniciar jogo
#     DJ - Detalhes do jogo
#     D + 1/2 Nomes - Desistir
#     CP + Nome + TamanhoPeça + Posição + (Sentido) - Colocar peça
#     V - Visualizar resultado
#     G - Gravar
#     L - Ler
#     X - Sair ''')
#     op1 = input("Digite uma opção: ")  # Opção 1


