'''
There is a rabbit that starts in the middle of an n x m matrix, n > 0, m > 0. Each element of a matrix is an integer
representing points gained for being on the spot. If there are multiple possible "middles" then choose the one which
has the highest point value to start on. On each iteration, the rabbit can move up, left, right, or down. The rabbit
will always move to the next spot with the highest point value and will "consume" those points (set the point value
in that position to 0). The rabbit spots when all positions around it are 0s. Calculate how many points the rabbit
will score for a given m x n matrix.

Example
Input
5, 7, 8, 6, 3 0, 0, 7, 0, 4 4, 6, 3, 4, 9 3, 1, 0, 5, 8

Output
27
'''


def hungry_rabbit(garden) :

    def hungry_rabbit_utils(garden, row, col):

        max = 0
        next_row = None
        next_col = None

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            next_x = dx + row
            next_y = dy + col
            if 0 <= next_x < len(garden) and 0<= next_y < len(garden[row]) and garden[next_x][next_y] > max:
                max = garden[next_x][next_y]
                next_row = next_x
                next_col = next_y

        carrots = garden[row][col]
        garden[row][col] = 0
        if max > 0 and next_row is not None and next_col is not None:
            carrots += hungry_rabbit_utils(garden, next_row, next_col)
        return carrots


    def findMid(garden):
        row_options = [len(garden) // 2, len(garden) // 2]
        col_options = [len(garden[0]) // 2, len(garden[0]) // 2]

        if len(garden) % 2 == 0:
            row_options[0] -= 1
        if len(garden[0]) % 2 == 0:
            col_options[0] -= 1

        max = 0
        row = None
        col = None
        for rowOption in row_options:
            for colOption in col_options:
                if garden[rowOption][colOption] > max:
                    max = garden[rowOption][colOption]
                    row = rowOption
                    col = colOption
        return row, col


    if len(garden) == 0 or len((garden[0])) == 0:
        return 0
    copy_garden = [[garden[i][j] for j in range(len(garden[0]))] for i in range(len(garden))]
    row, col = findMid(copy_garden)
    print(copy_garden)
    if row is None or col is None:
        return 0
    return hungry_rabbit_utils(copy_garden, row, col)



if __name__ == "__main__":
    garden = [
        [5, 7, 8, 6, 3],
        [0, 0, 7, 0, 4],
        [4, 6, 3, 4, 9],
        [3, 1, 0, 5, 8]
    ]

    print(hungry_rabbit(garden)) # 27