# player 1 is X
# player 2 is O (capital o, the letter)
# initalize a global list that holds a game board
import random
import sys
import copy

game_board = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

# game_board = [[' ', 'X', ' '],
#               ['O', 'X', 'X'],
#               ['O', ' ', 'O']]

game_state = 'Game not finished'  # Draw, O wins, X wins





def print_game_board():
    # global game_board
    print('-' * 9)
    for row in game_board:
        row_reps = '| '
        for e in row:
            row_reps = row_reps + e + ' '
        row_reps = row_reps + '|'
        print(row_reps)
    print('-' * 9)


def is_cell_free(row_coor, column_coor):
    if game_board[row_coor-1][column_coor-1] == ' ':
        return True
    else:
        return False


# def starting_game_board_input():
#     start_str = input('Enter initial state of the game board >')
#     for i in range(3):
#         for j in range(3):
#             if start_str[3*i+j] == '_':
#                 game_board[i][j] = ' '
#             else:
#                 game_board[i][j] = start_str[3*i+j]


def player_input():
    players_move = input('Enter the coordinates:')
    players_move = ' '.join(players_move.split())
    players_move_ = players_move.split(' ')
    # if len(players_move_) != 2:
    #     print('Enter the coordinates divided with a space.')
    #     return []
    try:
        row_coor = int(players_move_[0])
        column_coor = int(players_move_[1])
    except ValueError as e:
        print('You should enter numbers!')
        return []
    except IndexError:
        print('You should enter numbers!')
        return []
    if 0 < row_coor < 4 and 0 < column_coor < 4:
        pass
    else:
        print('Coordinates should be from 1 to 3!')
        return []
    if is_cell_free(row_coor, column_coor):
        pass
    else:
        print('This cell is occupied! Choose another one!')
        return []
    return [row_coor, column_coor]


def check_list_for_win(list_of_tree):
    """
    returns unique element, as a list, in case all elements in list are the same or
    returns an empty list.
    :param list_of_tree: list to check
    :return: list
    """
    unique_elements = []
    for e in list_of_tree:
        if e not in unique_elements:
            unique_elements.append(e)
    if len(unique_elements) == 1 and unique_elements[0] != ' ':
        return unique_elements
    else:
        return []


def check_game_state(test_game_board=None, test=False):
    global game_state
    global game_board
    if test_game_board is None:
        test_game_board = game_board
    # check rows
    list_of_tree = []
    for i in range(3):
        list_of_tree = test_game_board[i]
        check = check_list_for_win(list_of_tree)
        if len(check) == 1:
            if not test:
                game_state = check[0] + ' wins'
                print(game_state)
                return
            else:
                return 'win'

    # check columns
    for i in range(3):
        list_of_tree = []
        for j in range(3):
            list_of_tree.append(test_game_board[j][i])
        check = check_list_for_win(list_of_tree)
        if len(check) == 1:
            if not test:
                game_state = check[0] + ' wins'
                print(game_state)
                return
            else:
                return 'win'

    # check diagonal 1
    list_of_tree = []
    for i in range(3):
        list_of_tree.append(test_game_board[i][i])
    check = check_list_for_win(list_of_tree)
    if len(check) == 1:
        if not test:
            game_state = check[0] + ' wins'
            print(game_state)
            return
        else:
            return 'win'

    # check diagonal 2
    list_of_tree = []
    for i in range(3):
        list_of_tree.append(test_game_board[i][-i-1])
    # print(list_of_tree)
    check = check_list_for_win(list_of_tree)
    if len(check) == 1:
        if not test:
            game_state = check[0] + ' wins'
            print(game_state)
            return
        else:
            return 'win'

    # all spots filled
    game_board_str = ''
    for i in range(3):
        for j in range(3):
            game_board_str = game_board_str + test_game_board[i][j]
    if ' ' not in game_board_str:
        if not test:
            game_state = 'Draw'
            print(game_state)
            return
        else:
            return 'Draw'

    if test:
        return 'continue'


# def move_symbol():
#     game_board_str = ''
#     nr_of_x = 0
#     nr_of_o = 0
#     for i in range(3):
#         for j in range(3):
#             if game_board[i][j] == 'X':
#                 nr_of_x = nr_of_x + 1
#             elif game_board[i][j] == 'O':
#                 nr_of_o = nr_of_o + 1
#     if nr_of_x == nr_of_o:
#         return 'X'
#     else:
#         return 'O'


def move_player_1(symbol):
    player_1_valid_input = False
    while not player_1_valid_input:
        player_1_input = player_input()
        # print(player_1_input)
        if player_1_input:
            player_1_valid_input = True
    game_board[player_1_input[0] - 1][player_1_input[1] - 1] = symbol


def move_ai_easy(symbol, print_msg=True):
    if print_msg:
        print('Making move level "easy"')
    # get idx of free cells
    list_idx_of_free_cells = []
    for i in range(3):
        for j in range(3):
            if is_cell_free(i+1, j+1):
                list_idx_of_free_cells.append([i, j])
    move = random.choice(list_idx_of_free_cells)
    game_board[move[0]][move[1]] = symbol


def move_ai_medium(symbol, symbols=('X', 'O'), print_msg=True):
    global game_board

    if print_msg:
        print('Making move level "medium"')

    possible_move = []
    for i in range(3):
        for j in range(3):
            if is_cell_free(i + 1, j + 1):
                possible_move.append([i, j])
    # random.shuffle(list_idx_of_free_cells)

    # block
    if symbol == symbols[0]:
        opponent_symbol = symbols[1]
    else:
        opponent_symbol = symbols[0]
    for move in possible_move:
        test_board = copy.deepcopy(game_board)
        test_board[move[0]][move[1]] = opponent_symbol
        test_res = check_game_state(test_board, test=True)
        if test_res == 'win':
            game_board[move[0]][move[1]] = symbol
            return

    # win
    for move in possible_move:
        test_board = copy.deepcopy(game_board)
        test_board[move[0]][move[1]] = symbol
        test_res = check_game_state(test_board, test=True)
        if test_res == 'win':
            game_board[move[0]][move[1]] = symbol
            return

    # do random
    move_ai_easy(symbol, print_msg=False)


def get_idx_of(lst, min_or_max=max):
    #print(lst)
    extreme = min_or_max(lst)
    for i in range(len(lst)):
        if lst[i] == extreme:
            return i


def minimax(new_game_board, turn_sign, symbols, verbose=False):
    """
    symbols = ( my-symbol, opponents-symbol)
    :param new_game_board:
    :param turn_sign: the turn that created the new_game_board
    :param symbols:
    :return:
    """
    if verbose:
        print('new_game_board', new_game_board)
    check = check_game_state(new_game_board, test=True)

    if check == 'win':
        # print(turn_sign)
        return turn_sign
    elif check == 'Draw':
        # print(0)
        return 0
    else:
        # check == continue
        # gen next moves
        #print('    the check was "continue"')
        free_cells = []
        for i in range(3):
            for j in range(3):
                if new_game_board[i][j] == ' ':
                    free_cells.append([i, j])
        # print('nr free cells', len(free_cells))
        move_scores = []
        for move in free_cells:
            # gen new game board
            next_board = copy.deepcopy(new_game_board)
            if turn_sign > 0:
                next_symbol = symbols[1]
            else:
                next_symbol = symbols[0]
            next_board[move[0]][move[1]] = next_symbol
            move_scores.append(minimax(next_board, turn_sign*-1, symbols))
        if verbose:
            print('move scores', move_scores, 'for sign', turn_sign*-1)

        if turn_sign*-1 > 0:
            return max(move_scores)
        else:
            # print('returned minimum')
            return min(move_scores)


def move_ai_hard(symbol, verbose=False):
    print('Making move level "hard"')
    global game_board
    # gen symbol-list
    if symbol == 'X':
        symbols = ['X', 'O']
    else:
        symbols = ['O', 'X']

    #gen possible new gameboards:
    free_cells = []
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == ' ':
                free_cells.append([i, j])
    move_scores = []
    for move in free_cells:
        next_board = copy.deepcopy(game_board)
        next_board[move[0]][move[1]] = symbol
        move_scores.append(minimax(next_board, +1, symbols, verbose))

    #print('move scores', move_scores)
    move_idx = get_idx_of(move_scores, max)
    if verbose:
        print('final', free_cells)
        print('final',move_scores)
        print('final',move_idx)

    # do best move
    move = free_cells[move_idx]
    # print('best move', move)
    game_board[move[0]][move[1]] = symbol


def game_loop(p1, p2):
    # check_game_state()
    # print(game_state)
    while game_state == 'Game not finished':
        p1('X')
        print_game_board()
        check_game_state()

        if 'wins' in game_state or 'Draw' in game_state:
            break

        p2('O')
        print_game_board()
        check_game_state()


def start_game():
    global player_modes
    start_input = input('Input command')
    cmds = start_input.split(' ')
    if cmds[0] == 'exit':
        sys.exit(0)
    try:
        player1 = player_modes[cmds[1]]
        player2 = player_modes[cmds[2]]
    except Exception as e:
        print('Bad parameters!')
        return start_game()
    # print(player1, player2)
    return player1, player2


player_modes = dict()
player_modes['user'] = move_player_1
player_modes['easy'] = move_ai_easy
player_modes['medium'] = move_ai_medium
player_modes['hard'] = move_ai_hard

if __name__ == '__main__':
    player1, player2 = start_game()
    print_game_board()
    game_loop(player1, player2)
