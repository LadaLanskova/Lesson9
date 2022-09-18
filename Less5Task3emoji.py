"""
Создайте программу для игры в ""Крестики-нолики"".
"""
from random import randint
import emoji

def field_printing(field: list):
    for i in range(len(field)):
        st_lel = ""
        for j in range(len(field)):
            st_lel += str(field[i][j])
        print(st_lel)

def user_input(coordinate: str) -> int: 
    inp = 0
    while inp/2 < 1 or inp/2 > 3:
        if coordinate == "a":
            n = input(f'Введите номер строки {coordinate} (1<={coordinate}<=3): ')
        else:
            n = input(f'Введите номер столбца {coordinate} (1<={coordinate}<=3): ')
        if n.isdigit():
            inp = 2 * int(n)
            if inp / 2 < 1 or inp / 2 > 3:
                print(f'Введено некорректное значение: {n}. Введите число от 1 до 3!')
        else:
            print(f'Введено некорректное значение: {n}. Введите число от 1 до 3!')
    return inp

def check_for_win(play_list: list, player: int):
    win = 0
    diag_down, dag_up = '', ''
    for i in range(2, len(play_list), 2):
        diag_down += play_list[i][i]
        dag_up += play_list[i][len(play_list)-i]
        line, column = '', ''
        for j in range(2, len(play_list), 2):
            line += play_list[i][j]
            column += play_list[j][i]
        win = max(win, line.count(simbol_dict[player]), 
            column.count(simbol_dict[player]))
    win = max(win, diag_down.count(simbol_dict[player]),
                dag_up.count(simbol_dict[player]))
    return win


field = [['  ', '  ', '  b1 ', '  ', ' b2 ', '  ', ' b3 ', '  '],
    ['  ', '  ---', '---', '---', '---', '---', '---', '----'],
        ['a1 ', ' | ', '    ', ' | ', '    ', ' | ', '    ', ' | '],
            ['  ', '  ---', '---', '---', '---', '---', '---', '----'],
                ['a2 ', ' | ', '    ', ' | ', '    ', ' | ', '    ', ' | '],
                    ['  ', '  ---', '---', '---', '---', '---', '---', '----'],
                        ['a3 ', ' | ', '    ', ' | ', '    ', ' | ', '    ', ' | '],
                            ['  ', '  ---', '---', '---', '---', '---', '---', '----']]

print("Здравствуйте! Вас приветствует игра Крестики - Нолики!\U0001F63A\n")


name1 = input('Введите имя первого игрока: ')
name2 = input(f'Введите имя второго игрока: ')
print()

flag = randint(0, 1)
if flag:
    player1 = name1
    player2 = name2

else:
    player1 = name1
    player2 = name2

print(f'Приятно познакомиться! Первым ходит {player1} и играет крестиками, {player2} играет ноликами! Поехали!\U0001F3C1\n')


move_dict = {1: f"Ход {player1}:", 0: f"ход {player2}:"}
simbol_dict = {1: ' \U0000274C ', 0: ' \U00002B55 '}
win_dict = {1: f'Крестики рулят! Победил {player1}!\U0001F3C6', 0: f'Нолики forever! Победил {player2}!\U0001F3C6'}
print()
field_printing(field)
print()
player_move = 1
win_flag = False
while player_move < 10 and not win_flag:
    player = player_move % 2
    move_flag = False
    while not move_flag:
        print(move_dict[player])
        print()
        a = user_input('a')
        b = user_input('b')
        if field[a][b] == "    ":
            field[a][b] = simbol_dict[player]
            move_flag = True
        else:
            print('Эта ячейка занята, выберите другую ячейку.\U0001F645\n')
    field_printing(field)
    print()
    if player_move > 4:    
        if check_for_win(field, player) == 3:
            win_flag = True
            print(win_dict[player])
    player_move += 1
if win_flag == False:
    print('Ничья! Победила дружба!\U0001F942')
