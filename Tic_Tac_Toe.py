# 2. Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

board = list(range(1, 10))
winning_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def get_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|') 
    print('-------------')


def take_input(player_token):
    while True:
        value = input(f'Where do you want to draw {player_token}?')
        if not (value in '123456789'):
            print('Try again')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('This cell is already occupied')
            continue
        board[value - 1] = player_token
        break


def check_win():
    for i in winning_comb:
        if (board[i[0]-1]) == (board[i[1]-1]) == (board[i[2]-1]):
            return board[i[1] - 1]
    else:
        return False


def main():
    count = 0
    while True:
        get_board()
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if count > 3:
            winner = check_win()
            if winner:
                get_board()
                print(f'{winner} won!')
                break
        count+=1
        if count > 8:
            get_board()
            print('Draw!')
            break

main()
