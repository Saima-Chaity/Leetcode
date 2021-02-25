'''Find all rectangles filled with 0

We have one 2D array, filled with zeros and ones. We have to find the starting point and ending point of all
rectangles filled with 0. It is given that rectangles are separated and do not touch each other however they
can touch the boundary of the array.A rectangle might contain only one element.

Examples:
input = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
Output:
[
  [2, 3, 3, 5], [3, 1, 5, 1], [5, 3, 6, 5]
]'''

def get_rectangle_coordinates(matrix):

    def findEnd(i, j, index):
        flag_row = 0
        flag_col = 0
        for m in range(i, row):
            if matrix[m][j] == 1:
                flag_row = 1
                break
            if matrix[m][j] == -1:
                continue

            for n in range(j, col):
                if matrix[m][n] == 1:
                    flag_col = 1
                    break
                matrix[m][n] = -1

        if flag_row == 1:
            output[index].append(m-1)
        else:
            output[index].append(m)

        if flag_col == 1:
            output[index].append(n - 1)
        else:
            output[index].append(n)

    row = len(matrix)
    col = len(matrix[0])
    output = []
    index = -1
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                output.append([i, j])
                index += 1
                findEnd(i, j, index)
    return output

tests = [

    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]

]

print(get_rectangle_coordinates(tests)) #[[2, 3, 3, 5], [3, 1, 5, 1], [5, 3, 6, 5]]

tests = [
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 0]
        ]

print(get_rectangle_coordinates(tests))
# [
#   [0, 1, 0, 1], [1, 2, 1, 2], [2, 3, 3, 5],
#   [3, 1, 4, 1], [5, 3, 5, 6], [7, 2, 7, 2],
#   [7, 6, 7, 6]
# ]