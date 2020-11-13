'''After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, but there's a rumour 
that all the free rooms are haunted! Since the CodeBots are quite superstitious, 
they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, 
your task is to return the total sum of all rooms that are suitable for the CodeBots 
(ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.'''

def matrixElementsSum(matrix):
    
    row = len(matrix)
    col = len(matrix[0])
    totalCost = 0
    i = 0
    j = 0
    while i < row and j < col:
        if matrix[i][j] == 0:
            for k in range(i, row):
                matrix[k][j] = 0

        j += 1
        if j == col and i < row:
            i += 1
            j = 0
    
    for i in range(row):
        for j in range(col):
            totalCost += matrix[i][j]
    return totalCost




