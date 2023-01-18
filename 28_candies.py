# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint

candies = 200
player_takes = 0
bot_takes = 0

def whose_turn():
    first_turn = randint(1, 2)
    if first_turn == 1:
        player_turn()
    else:
        bot_turn()


def player_turn():
    global candies
    global player_takes
    while True:
        try:
            player_takes = int(input('How many candies do you take? : '))
            if player_takes > 0 and player_takes < 29 and player_takes <= candies:
                break
        except:
            print('You should take no more than 28 candies! Try again: ')
    candies = candies - player_takes
    print(f'{candies} candies left')
    if candies > 0:
        bot_turn()
    else:
        print('You won!')
    

def bot_turn():
    global candies
    global bot_takes
    bot_takes = candies % 29 if candies % 29 != 0 else randint(1, 28)
    candies = candies - bot_takes
    print(f'Bot has taken {bot_takes} candies. \n{candies} candies left')
    if candies > 0:
        player_turn()
    else:
        print('Bot won!')

whose_turn()


# 2 PLAYERS



# from random import randint

# candies = 200
# player1_takes = 0
# player2_takes = 0

# def whose_turn():
#     first_turn = randint(1, 2)
#     if first_turn == 1:
#         player1_turn()
#     else:
#         player2_turn()
        

# def player1_turn():
#     global candies
#     global player1_takes
#     while True:
#         try:
#             player1_takes = int(input('Player 1, how many candies do you take? : '))
#             if player1_takes > 0 and player1_takes < 29 and player1_takes <= candies:
#                 break
#         except:
#             print('You should take no more than 28 candies! Try again: ')
#     candies = candies - player1_takes
#     print(f'{candies} candies left')
#     if candies > 0:
#         player2_turn()
#     else:
#         print('Player 1 won!')
    

# def player2_turn():
#     global candies
#     global player2_takes
#     while True:
#         try:
#             player2_takes = int(input('Player 2, how many candies do you take? : '))
#             if player2_takes > 0 and player2_takes < 29 and player2_takes <= candies:
#                 break
#         except:
#             print('You should take no more than 28 candies! Try again: ')
#     candies = candies - player2_takes
#     print(f'{candies} candies left')
#     if candies > 0:
#         player1_turn()
#     else:
#         print('Player 2 won!')

# whose_turn()