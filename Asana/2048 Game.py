import random
def startGame():
    matrix = [[0] * 4 for _ in range(4)]

    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    add_new_two(matrix)
    return matrix

def add_new_two(matrix):
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    while matrix[row][col] != 0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
    matrix[row][col] = 2
    print(matrix)

def getCurrentState(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                return 'Won'

    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return 'Game not over'

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == matrix[i+1][j] or matrix[i][j] == matrix[i][j+1]:
                return 'Game not over'

    for i in range(3):
        if matrix[i][3] == matrix[i+1][3]:
            return 'Game not over'

    for j in range(3):
        if matrix[3][j] == matrix[3][j+1]:
            return 'Game not over'
    return 'Lost'

def compress(matrix):
    changed = False
    new_matrix = [[0] * 4 for _ in range(4)]
    for i in range(4):
        position = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_matrix[i][position] = matrix[i][j]
                if j != position:
                    changed = True
                position += 1
    return new_matrix, changed

def merge(matrix):
    changed = False
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0:
                matrix[i][j] = matrix[i][j] * 2
                matrix[i][j+1] = 0
                changed = True
    return matrix, changed

def reverse(matrix):
    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[i][3-j])
    return new_matrix

def transpose(matrix):
    new_matrix = []
    for i in range(4):
        new_matrix.append([])
        for j in range(4):
            new_matrix[i].append(matrix[j][i])
    return new_matrix

def move_left(matrix):
    new_matrix, changed1 = compress(matrix)
    new_matrix, changed2 = merge(new_matrix)
    changed = changed1 or changed2
    new_matrix, temp = compress(new_matrix)
    return new_matrix, changed

def move_right(matrix):
    new_matrix = reverse(matrix)
    new_matrix, changed = move_left(new_matrix)
    new_matrix = reverse(new_matrix)
    return new_matrix, changed

def move_up(matrix):
    new_matrix = transpose(matrix)
    new_matrix, changed = move_left(new_matrix)
    new_matrix = transpose(new_matrix)
    return new_matrix, changed

def move_down(matrix):
    new_matrix = transpose(matrix)
    new_matrix, changed = move_right(new_matrix)
    new_matrix = transpose(new_matrix)
    return new_matrix, changed

matrix = startGame()
while True:
    x = input('Press the command : ')
    if x == 'W' or x == 'w':
        matrix, flag = move_up(matrix)
        status = getCurrentState(matrix)
        print(status)
        if status == 'Game not over':
            add_new_two(matrix)
        else:
            break
    elif x == 'S' or x == 's':
        matrix, flag = move_down(matrix)
        status = getCurrentState(matrix)
        print(status)
        if status == 'Game not over':
            add_new_two(matrix)
        else:
            break
    elif x == 'A' or x == 'a':
        matrix, flag = move_left(matrix)
        status = getCurrentState(matrix)
        print(status)
        if status == 'Game not over':
            add_new_two(matrix)
        else:
            break
    elif x == 'D' or x == 'd':
        matrix, flag = move_right(matrix)
        status = getCurrentState(matrix)
        print(status)
        if status == 'Game not over':
            add_new_two(matrix)
        else:
            break
    else:
        print('Invalid keyword')
    print(matrix)