import random
import time


def declare(x, y):
    # definovanie boardu
    for i in range(1, board_size + 1):
        new = []
        for j in range(1, board_size + 1):
            new.append(0)
        chess_board.append(new)


def get_possible_steps(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possible_steps = []
    for i in range(8):
        if 0 <= x + pos_x[i] <= board_size - 1 and y + pos_y[i] >= 0 and y + pos_y[
            i] <= board_size - 1 and \
                chess_board[x + pos_x[i]][y + pos_y[i]] == 0:
            possible_steps.append([x + pos_x[i], y + pos_y[i]])

    return possible_steps


def lets_tour_with_heuristic(x, y, counter, board_size, chess_board):

    chess_board[x][y] = counter
    if counter == board_size ** 2:
        return True
    options = get_possible_steps(x, y)
    if options:
        actual_step = options[0]
        for i in options:
            if len(get_possible_steps(i[0], i[1])) <= len(get_possible_steps(actual_step[0], actual_step[1])):
                actual_step = i
        counter += 1
        if lets_tour_with_heuristic(actual_step[0], actual_step[1], counter, board_size, chess_board):
            return True
        else:
            counter -= 1

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

board_size = 7

chess_board = []
counter = 1
x = random.randrange(board_size)
y = random.randrange(board_size)


declare(x, y)

start = time.time()
lets_tour_with_heuristic(x, y, counter, board_size, chess_board)
end = time.time()
for i in range(board_size):
    for j in range(board_size):
        print("{0:>3}".format(chess_board[i][j]), end=" ")
    print()
print("Potrebny cas s heuristikou: " + str((end-start)*1000)+"ms")

"""
chess_board = []
counter = 1
declare(x, y)
start = time.time()
lets_tour_without_heuristic(x, y, counter, board_size, chess_board)
end = time.time()

for i in range(board_size):
    for j in range(board_size):
        print("{0:>3}".format(chess_board[i][j]), end=" ")
    print()
print("Potrebny cas bez heuristiky: " + str((end-start)*1000)+"ms")
"""