board = [' ' for x in range(10)]

def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def check_win(board, player):
    return (
        (board[1] == player and board[2] == player and board[3] == player) or
        (board[4] == player and board[5] == player and board[6] == player) or
        (board[7] == player and board[8] == player and board[9] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[3] == player and board[6] == player and board[9] == player) or
        (board[1] == player and board[5] == player and board[9] == player) or
        (board[3] == player and board[5] == player and board[7] == player)
    )

def check_tie(board):
    return ' ' not in board[1:]

def get_move(board, player):
    move = input(f"Jogador {player}, escolha uma posição de 1 a 9: ")
    while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or board[int(move)] != ' ':
        move = input(f"Jogador {player}, escolha uma posição válida de 1 a 9 que esteja vazia: ")
    return int(move)

def play():
    player = 'X'
    while True:
        print_board(board)
        move = get_move(board, player)
        board[move] = player
        if check_win(board, player):
            print_board(board)
            print(f"Parabéns, jogador {player} ganhou o jogo!")
            break
        if check_tie(board):
            print_board(board)
            print("Empate!")
            break
        player = 'O' if player == 'X' else 'X'

play()
