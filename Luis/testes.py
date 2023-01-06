board = [[' ' for _ in range(7)] for _ in range(6)]

def print_board():
    print('1 2 3 4 5 6 7')
    for row in board:
        print('|'.join(row))

def make_move(player, column):
    column -= 1
    for i in range(5, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = player
            return
    print("A coluna encontra-se completa, escolhe outra coluna.")

def has_won(player):
    # Verifica vitória horizontal
    for row in board:
        if row.count(player) == 4:
            return True
    # Verifica vitória vertical
    for col in range(7):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player and board[3][col] == player:
            return True
    # Verifica vitória diagonal
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    for row in range(3):
        for col in range(4):
            if board[row+3][col] == player and board[row+2][col+1] == player and board[row+1][col+2] == player and board[row][col+3] == player:
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



