import sys
import time

sys.setrecursionlimit(1000000)


def declare():
    # definovanie boardu
    for i in range(1, board_size + 1):
        new = []
        for j in range(1, board_size + 1):
            new.append(0)
        chess_board.append(new)


def get_possible_steps(x, y):
    pos_x = (2, -2, 1, -1, 2, -2, 1, -1)
    pos_y = (1, 1, 2, 2, -1, -1, -2, -2)
    possible_steps = []
    for i in range(len(pos_x)):
        if 0 <= x + pos_x[i] <= board_size - 1 and y + pos_y[i] >= 0 and y + pos_y[
            i] <= board_size - 1 and \
                chess_board[x + pos_x[i]][y + pos_y[i]] == 0:
            possible_steps.append([x + pos_x[i], y + pos_y[i]])

    return possible_steps


def lets_tour_with_heuristic(x, y, counter, board_size, chess_board, start):
    end = time.time()
    if end - start > 15:
        return True
    chess_board[x][y] = counter
    if counter == board_size ** 2:
        return True
    options = get_possible_steps(x, y)
    if options:
        new = []
        number_of_options = []
        for i in options:
            # if len(get_possible_steps(i[0], i[1])) <= len(get_possible_steps(actual_step[0], actual_step[1])):
            # actual_step = i
            number_of_options.append(len(get_possible_steps(i[0], i[1])))
        # actual_step = options[order_options.index(min(order_options))]
        counter += 1
        # index = options.index(actual_step)

        while options:
            new.append(options[number_of_options.index(min(number_of_options))])
            del options[number_of_options.index(min(number_of_options))]
            del number_of_options[number_of_options.index(min(number_of_options))]

        for i in new:
            tour_value = lets_tour_with_heuristic(i[0], i[1], counter, board_size, chess_board, start)
            if tour_value:
                return True
            # counter -= 1

    if counter == 1:
        chess_board[x][y] = 1
        return False
    else:
        chess_board[x][y] = 0
        return False


def lets_tour_without_heuristic(x, y, counter, board_size, chess_board):
    chess_board[x][y] = counter
    if counter == board_size ** 2:
        return True
    options = get_possible_steps(x, y)
    if options:
        for i in options:
            counter += 1
            if lets_tour_without_heuristic(i[0], i[1], counter, board_size, chess_board):
                return True
            else:
                counter -= 1

    if counter == 1:
        chess_board[x][y] = 1
        return False
    else:
        chess_board[x][y] = 0
        return False


board_size = 10
for k in range(1):
    chess_board = []
    counter = 1

    x, y = 0,0

    declare()
    step_count = 0

    start = time.time()
    # lets_tour_with_heuristic(x, y, counter, board_size, chess_board, step_count)
    lets_tour_with_heuristic(x, y, counter, board_size, chess_board, start)
    end = time.time()
    print("Začiatočna pozícia = [" + str(x) + ", " + str(y) + "]")
    for i in range(board_size):
        for j in range(board_size):
            print("{0:>3}".format(chess_board[j][i]), end=" ")
        print()
    if end - start > 15:
        print("Program nestihol najst riešenie do 15 sekund")
    else:
        print("Potrebny cas s heuristikou: " + str((end - start) * 1000) + "ms")
"""
    chess_board = []
    counter = 1
    declare()
    start = time.time()
    print(lets_tour_without_heuristic(x, y, counter, board_size, chess_board))
    end = time.time()

    for i in range(board_size):
        for j in range(board_size):
            print("{0:>3}".format(chess_board[i][j]), end=" ")
        print()
    print("Potrebny cas bez heuristiky: " + str((end - start) * 1000) + "ms")
    print("--------------------------------------------")
"""
