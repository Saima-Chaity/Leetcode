'''Find the longest path in a matrix with given constraints

Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) such that
all cells along the path are in increasing order with a difference of 1.

We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or
(i, j-1) with the condition that the adjacent cells have a difference of 1.

Example:

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9. '''


def longestIncreasingPath(matrix):
    def dfs(i, j):
        if cache[i][j]:
            return cache[i][j]
        result = 0
        for dx, dy in directions:
            xi = i + dx
            yj = j + dy
            if 0 <= xi < rows and 0 <= yj < cols and matrix[xi][yj]+1 == matrix[i][j]:
                result = max(result, dfs(xi, yj))
        cache[i][j] = result + 1
        return cache[i][j]

    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    longestPath = float('-inf')
    cache = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result = dfs(i, j)
            longestPath = max(longestPath, result)
    return longestPath

matrix = [[1, 2, 9],
    [5, 3, 8],
    [4, 6, 7]]
print("Length of the longest path is ", longestIncreasingPath(matrix))