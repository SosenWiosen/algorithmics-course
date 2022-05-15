import os
import platform
import random as rand


def main():
    field = [[' ' for _ in range(3)] for _ in range(3)]

    available_moves = [(i, j) for i in range(3) for j in range(3)]

    with_computer_str = input('Do you want to play with a computer? (y) ')
    with_computer = False
    if with_computer_str == 'y':
        with_computer = True

    curr_player = 'o'
    moves = 9
    game_has_ended = False
    while not game_has_ended:
        print_playing_field(field)

        print('Enter your move, player ', curr_player, ':')
        has_moved = False
        while not has_moved:
            has_moved = True
            if not with_computer or curr_player == 'o':
                try:
                    row = int(input('Row? '))
                    column = int(input('Column? '))
                    move(row, column, curr_player, field)
                    for av_move in available_moves:
                        if av_move[0] == row and av_move[1] == column:
                            available_moves.remove(av_move)
                except TypeError:
                    print("That's not a correct move!")
                    has_moved = False
                except ValueError:
                    print("Wrong input!!")
                    has_moved = False
            else:
                chosen_move = rand.choice(available_moves)
                move(chosen_move[0], chosen_move[1], 'x', field)
                available_moves.remove(chosen_move)
        if curr_player == 'o':
            curr_player = 'x'
        else:
            curr_player = 'o'
        status = check_if_game_end(field)
        moves -= 1
        if status != '':
            print_playing_field(field)
            print(status)
            game_has_ended = True
        elif moves == 0:
            print_playing_field(field)
            print('No one has won!')
            game_has_ended = True
    print('GG')


def clear_console():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def check_if_game_end(field):
    for row in field:
        p0 = row[0]
        if p0 == ' ':
            continue
        the_same = True
        for cell in row:
            if cell != p0:
                the_same = False
                break
        if the_same:
            return '%s has won' % p0

    for col in range(3):
        p0 = field[0][col]
        if p0 == ' ':
            continue
        the_same = True
        for row in range(3):
            if field[row][col] != p0:
                the_same = False
                break
        if the_same:
            return '%s has won' % p0
    p0 = field[1][1]
    if p0 == ' ':
        return ''
    the_same_d = True
    the_same_a = True
    for pos in range(3):
        if field[pos][pos] != p0:
            the_same_d = False
        if field[pos][2 - pos] != p0:
            the_same_a = False
    if the_same_a or the_same_d:
        return '%s has won' % p0
    return ''


def print_playing_field(field):
    clear_console()
    print_line()

    for rows in field:
        print('| ', end='')
        for cell in rows:
            print(cell, end='')
            print_spacer()
        print('')
        print_line()


def move(row, col, char, field):
    if 0 > row or row > 2 or col < 0 or col > 2:
        raise TypeError
    elif char != 'x' and char != 'o':
        raise TypeError
    elif field[row][col] != ' ':
        raise TypeError
    field[row][col] = char


def print_line():
    for i in range(12):
        print('-', end='')
    print('-')


def print_spacer():
    print(' | ', end='')


if __name__ == '__main__':
    main()
