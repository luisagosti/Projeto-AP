# # Get board width and height from user
# width = int(input("Enter the width of the board: "))
# height = int(input("Enter the height of the board: "))

# # Generate board with the specified width and height
# board = [[' ' for _ in range(width)] for _ in range(height)]

# def print_board():
#     # Print the column numbers
#     print(' '.join([str(i+1) for i in range(width)]))
#     for row in board:
#         print('|'.join(row))

# def make_move(player, column):
#     column -= 1
#     for i in range(height-1, -1, -1):
#         if board[i][column] == ' ':
#             board[i][column] = player
#             return
#     print("A coluna encontra-se completa, escolhe outra coluna.")

# def has_won(player):
#     # Check for horizontal win
#     for row in board:
#         if row.count(player) == width:
#             return True
    
#     # Check for vertical win
#     for col in range(width):
#         if all(board[row][col] == player for row in range(height)):
#             return True
    
#     # Check for diagonal win
#     for row in range(height-3):
#         for col in range(width-3):
#             if all(board[row+i][col+i] == player for i in range(4)):
#                 return True
#             if all(board[row+3-i][col+i] == player for i in range(4)):
#                 return True
#     return False


# def main():
#     player = 'X'
#     while True:
#         print_board()
#         column = int(input(f"{player}, escolhe uma coluna: "))
#         make_move(player, column)
#         if has_won(player):
#             print_board()
#             print(f"{player} Venceu!")
#             break
#         player = 'O' if player == 'X' else 'X'

# main() 

# # Get board width and height from user
# width = int(input("Enter the width of the board: "))
# height = int(input("Enter the height of the board: "))

# # Get player names
# player1_name = input("Enter player 1 name: ")
# player2_name = input("Enter player 2 name: ")

# # Generate board with the specified width and height
# board = [[' ' for _ in range(width)] for _ in range(height)]

# def print_board():
#     # Print the column numbers
#     print(' '.join([str(i+1) for i in range(width)]))
#     for row in board:
#         print('|'.join(row))

# # def make_move(player, column):
# #     column -= 1
# #     for i in range(height-1, -1, -1):
# #         if board[i][column] == ' ':
# #             board[i][column] = player
# #             return
# #     print("A coluna encontra-se completa, escolhe outra coluna.")
# def make_move(player, column):
#     column -= 1
#     for i in range(height-1, -1, -1):
#         if board[i][column] == ' ':
#             if player == player1_name:
#                 board[i][column] = 'X'
#             else:
#                 board[i][column] = 'O'
#             return
#     print("A coluna encontra-se completa, escolhe outra coluna.")

# # def has_won(player):
# #     # Check for horizontal win
# #     for row in board:
# #         if row.count(player) == width:
# #             return True
    
# #     # Check for vertical win
# #     for col in range(width):
# #         if all(board[row][col] == player for row in range(height)):
# #             return True
    
# #     # Check for diagonal win
# #     for row in range(height-3):
# #         for col in range(width-3):
# #             if all(board[row+i][col+i] == player for i in range(4)):
# #                 return True
# #             if all(board[row+3-i][col+i] == player for i in range(4)):
# #                 return True
# #     return False

# def has_won(player):
#     # Check for horizontal win
#     for row in board:
#         if row.count(player) == width:
#             return True
    
#     # Check for vertical win
#     for col in range(width):
#         if all(board[row][col] == player for row in range(height)):
#             return True
    
#     # Check for diagonal win
#     for row in range(height-3):
#         for col in range(width-3):
#             if all(board[row+i][col+i] == player for i in range(4)):
#                 return True
#             if all(board[row+3-i][col+i] == player for i in range(4)):
#                 return True
#     return False


# def main():
#     player1 = player1_name
#     player2 = player2_name
#     while True:
#         print_board()
#         if player1 == player1_name:
#             column = int(input(f"{player1}, escolhe uma coluna: "))
#             make_move(player1_name, column)
#             if has_won(player1_name):
#                 print_board()
#                 print(f"{player1} Venceu!")
#                 break
#             player1, player2 = player2, player1
#         else:
#             column = int(input(f"{player2}, escolhe uma coluna: "))
#             make_move(player2_name, column)
#             if has_won(player2_name):
#                 print_board()
#                 print(f"{player2} Venceu!")
#                 break
#             player1, player2 = player2, player1

# main() 




# # Get board width and height from user
# width = int(input("Enter the width of the board: "))
# height = int(input("Enter the height of the board: "))

# # Generate board with the specified width and height
# board = [[' ' for _ in range(width)] for _ in range(height)]

# def print_board():
#     # Print the column numbers
#     print(' '.join([str(i+1) for i in range(width)]))
#     for row in board:
#         print('|'.join(row))

# def make_move(player, column):
#     column -= 1
#     for i in range(height-1, -1, -1):
#         if board[i][column] == ' ':
#             board[i][column] = player
#             return
#     print("A coluna encontra-se completa, escolhe outra coluna.")

# def has_won(player):
#     # Check for horizontal win
#     for row in board:
#         if row.count(player) == width:
#             return True
    
#     # Check for vertical win
#     for col in range(width):
#         if all(board[row][col] == player for row in range(height)):
#             return True
    
#     # Check for diagonal win
#     for row in range(height):
#         for col in range(width):
#             if row > height - 4 or col > width - 4:
#                 continue
#             if all(board[row+i][col+i] == player for i in range(4)):
#                 return True
#             if all(board[row+3-i][col+i] == player for i in range(4)):
#                 return True
#     return False



# def main():
#     player = 'X'
#     while True:
#         print_board()
#         column = int(input(f"{player}, escolhe uma coluna: "))
#         make_move(player, column)
#         if has_won(player):
#             print_board()
#             print(f"{player} Venceu!")
#             break
#         player = 'O' if player == 'X' else 'X'

# main() 


# Get board width and height from user
width = int(input("Enter the width of the board: "))
height = int(input("Enter the height of the board: "))

# Get the number of sequenced pieces needed to win
sequenced_pieces = int(input("Enter the number of sequenced pieces needed to win: "))

# Special pieces
special_Pieces = []
number_SpecialPieces = int(input("Digite o numero de peças especiais: "))
for i in len(number_SpecialPieces):
    special_Pieces[i] = int(input("Indique o tamanho da peça: "))



# Generate board with the specified width and height
board = [[' ' for _ in range(width)] for _ in range(height)]

def print_board():
    # Print the column numbers
    print(' '.join([str(i+1) for i in range(width)]))
    for row in board:
        print('|'.join(row))

def make_move(player, column):
    column -= 1
    for i in range(height-1, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = player
            return
    print("A coluna encontra-se completa, escolhe outra coluna.")

def has_won(player):
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


def main():
    player = 'X'
    while True:
        print_board()
        column = int(input(f"{player}, escolhe uma coluna: "))
        make_move(player, column)
        if has_won(player):
            print_board()
            print(f"{player} Venceu!")
            break
        player = 'O' if player == 'X' else 'X'

main()
