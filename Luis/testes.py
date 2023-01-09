
# Get board width and height from user
width = int(input("Enter the width of the board: "))
height = int(input("Enter the height of the board: "))

# Get the number of sequenced pieces needed to win
sequenced_pieces = int(input("Enter the number of sequenced pieces needed to win: "))


# Create a list to store the special pieces
special_pieces = []

# Get the number and size of special pieces from the user
num_special_pieces = int(input("Enter the number of special pieces: "))
for i in range(num_special_pieces):
    special_piece_size = int(input("Enter the size of special piece {} (in number of sequenced pieces): ".format(i+1)))
    special_pieces.append(special_piece_size)

# Generate board with the specified width and height
board = [[' ' for _ in range(width)] for _ in range(height)]

def print_board():
    # Print the column numbers
    print(' '.join([str(i+1) for i in range(width)]))
    for row in board:
        print('|'.join(row))

def make_move(player, column, use_special_piece=False, special_piece_index=None):
    column -= 1
    if use_special_piece:
        # Add the special piece
        special_piece_size = special_pieces[special_piece_index]
        for i in range(column, column+special_piece_size):
            for j in range(height-1, -1, -1):
                if i < width and board[j][i] == ' ':
                    board[j][i] = player
                    break
        else:
            print("A coluna encontra-se completa, escolhe outra coluna.")
            return
    else:
        for i in range(height-1, -1, -1):
            if board[i][column] == ' ':
                board[i][column] = player
                return
        print("A coluna encontra-se completa, escolhe outra coluna.")

def has_won(player):
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


def main():
    player = 'X'
    while True:
        print_board()
        column = int(input(f"{player}, escolhe uma coluna: "))
        use_special_piece = False
        special_piece_index = None
        if column == 0:
            print("Escolhe qual peça especial queres usar:")
            for i, special_piece in enumerate(special_pieces):
                print("{}: {} sequencias".format(i+1, special_piece))
            special_piece_index = int(input("Peça especial: ")) - 1
            use_special_piece = True
            column = int(input("Em que coluna queres jogar a peça especial: "))
        elif column < 0 or column > width:
            print("Coluna inválida, escolhe outra coluna.")
            continue
        make_move(player, column, use_special_piece=use_special_piece, special_piece_index=special_piece_index)
        if has_won(player):
            print_board()
            print(f"{player} Venceu!")
            break
        player = 'O' if player == 'X' else 'X'

main()










