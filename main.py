import random

""""
def declare():
    # definovanie boardu
    for i in range(1, board_size + 1):
        new = []
        for j in range(1, board_size + 1):
            new.append([j, i])
        board.append(new)

    # definovanie navstivenych suradnic
    for i in range(1, (board_size + 1) * (board_size + 1)):
        visited.append(0)


steps = 1
x = 0


def moving(steps, x):
    count = 0

    if steps != 1:
        x += 1
        knight[0] += moves[x][0]
        knight[1] += moves[x][1]

    for i in range(board_size):
        for j in range(board_size):
            if knight == board[i][j]:
                if visited[count] == 0 and (knight[0] >= 1 or knight[0] <= board_size or knight[1] >= 1 or knight[1] <= board_size):
                    visited[count] = steps
                    steps += 1
                    count = 0

                    if x == 7:
                        x = 0

                    moving(steps, x)
                else:
                    moving(steps, x)
            count += 1


board_size = 8
moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

board = []
visited = []

# startovna pozicia
knight = [random.randrange(1, board_size + 1), random.randrange(1, board_size + 1)]
#knight = [2, 5]

declare()

"""
""""
for i in range(board_size):
    for j in range(board_size):
        print(board[i][j], end="")
    print()
"""
"""
print("Knight's starting point: (" + str(knight[0]) + "; " + str(knight[1]) + ")")

# zaciatocny bod
moving(steps, x)

# knight[0] += moves[1][0]
# knight[1] += moves[1][1]

# print(moves)
# print("Knight's next point: (" + str(knight[0]) + "; " + str(knight[1]) + ")")

c = 0
for i in range(board_size):
    for j in range(board_size):
        print("{0:>2}".format(visited[c]), end=" ")
        c += 1
    print()
"""
# nie moje
"""
chess_board = [[1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]


def print_board():
    for i in range(8):
        for j in range(8):
            print("{0:>3}".format(chess_board[i][j]), end=" ")
        print("\n")


def get_possibilities(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        if x + pos_x[i] >= 0 and x + pos_x[i] <= 7 and y + pos_y[i] >= 0 and y + pos_y[i] <= 7 and \
                chess_board[x + pos_x[i]][y + pos_y[i]] == 0:
            possibilities.append([x + pos_x[i], y + pos_y[i]])

    return possibilities


def solve():
    counter = 2
    x = 0
    y = 0
    for i in range(63):
        pos = get_possibilities(x, y)
        minimum = pos[0]
        for p in pos:
            if len(get_possibilities(p[0], p[1])) <= len(get_possibilities(minimum[0], minimum[1])):
                minimum = p
        x = minimum[0]
        y = minimum[1]
        chess_board[x][y] = counter
        counter += 1


solve()
print_board()
"""


def declare(x, y):
    # definovanie boardu
    for i in range(1, board_size + 1):
        new = []
        for j in range(1, board_size + 1):
            new.append(0)
        chess_board.append(new)
    starting_point(x, y)


def starting_point(x, y):
    chess_board[x][y] = 1


def get_possibilities(x, y):
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []
    for i in range(8):
        if x + pos_x[i] >= 0 and x + pos_x[i] <= board_size - 1 and y + pos_y[i] >= 0 and y + pos_y[
            i] <= board_size - 1 and \
                chess_board[x + pos_x[i]][y + pos_y[i]] == 0:
            possibilities.append([x + pos_x[i], y + pos_y[i]])

    return possibilities


board_size = 5

chess_board = []
counter = 2
x = random.randrange(board_size)
y = random.randrange(board_size)

declare(x, y)
x_prev = 0
y_prev = 0
pos_prev = []
minimum_prev = []

while counter != board_size ** 2 + 1:
    pos = get_possibilities(x, y)
    if not pos:
        pos = pos_prev
        pos.remove(minimum_prev)
        chess_board[x][y] = 0
        pos = get_possibilities(x_prev, y_prev)

    minimum = pos[0]
    for p in pos:
        if len(get_possibilities(p[0], p[1])) <= len(get_possibilities(minimum[0], minimum[1])):
            minimum = p

    minimum_prev = minimum
    pos_prev = pos
    x_prev = x
    y_prev = y
    x = minimum[0]
    y = minimum[1]

    chess_board[x][y] = counter
    counter += 1

for i in range(board_size):
    for j in range(board_size):
        print("{0:>3}".format(chess_board[i][j]), end=" ")
    print()
print("--------------------------------")
