# Game of Life - https://leetcode.com/problems/game-of-life/
'''According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised
by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight
neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is
created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur
simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

        copy_board = [[board[i][j] for j in range(col)] for i in range(row)]

        for i in range(row):
            for j in range(col):
                live_neighbour = 0
                for x, y in direction:
                    next_x = x + i
                    next_y = y + j
                    if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col and copy_board[next_x][
                        next_y] == 1:
                        live_neighbour += 1
                if copy_board[i][j] == 1 and (live_neighbour > 3 or live_neighbour < 2):
                    board[i][j] = 0
                if copy_board[i][j] == 0 and live_neighbour == 3:
                    board[i][j] = 1
