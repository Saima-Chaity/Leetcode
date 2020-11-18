# Minesweeper - https://leetcode.com/problems/minesweeper/
'''Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine,
'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no
adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents
how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'),
return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and
all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8')
representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
'''


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        def getIndexes(click_x, click_y):
            count = 0
            output = []
            for dx, dy in direction:
                x = dx + click_x
                y = dy + click_y
                if 0 <= x < row and 0 <= y < col:
                    if board[x][y] == 'M':
                        count += 1
                    elif board[x][y] == 'E':
                        output.append((x, y))

            if count == 0:
                return count, output
            else:
                return count, []

        row = len(board)
        col = len(board[0])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        click_x, click_y = click[0], click[1]
        if board[click_x][click_y] == 'M':
            board[click_x][click_y] = 'X'
            return board
        else:
            if board[click_x][click_y] == 'E':
                stack = []
                visited = set()
                stack.append((click_x, click_y))
                while stack:
                    i, j = stack.pop()
                    if (i, j) not in visited:
                        visited.add((i, j))
                        mimes, indexes = getIndexes(i, j)
                        if mimes:
                            board[i][j] = str(mimes)
                        else:
                            board[i][j] = 'B'
                        stack += indexes
            return board

