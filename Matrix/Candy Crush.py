'''Candy Crush - https://leetcode.com/problems/candy-crush/

This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] represents the
type of candy. A value of board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. Now, you need to
restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, crush them all
at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these
candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the stable board.

Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],
[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],
[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
'''


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # O(m*n)^2 time and O(m*n) space
        self.row = len(board)
        self.col = len(board[0])
        while True:
            crushed = set()
            for i in range(self.row):
                for j in range(self.col):
                    if board[i][j] == 0:
                        continue
                    self.getCrushCandyCount(i, j, crushed, board)
            if len(crushed) >= 3:
                self.dropCandy(crushed, board)
            else:
                break
        return board

    def getCrushCandyCount(self, i, j, crushed, board):
        if 0 < i < self.row - 1 and board[i][j] == board[i - 1][j] == board[i + 1][j]:
            crushed.add((i, j))
            crushed.add((i + 1, j))
            crushed.add((i - 1, j))

        if 0 < j < self.col - 1 and board[i][j] == board[i][j - 1] == board[i][j + 1]:
            crushed.add((i, j))
            crushed.add((i, j + 1))
            crushed.add((i, j - 1))

    def dropCandy(self, crushed, board):
        # check column by column
        for j in range(self.col):
            temp = []
            for i in range(self.row):
                if board[i][j] and (i, j) not in crushed:
                    temp.append(board[i][j])

            for i in range(self.row - 1, -1, -1):
                if temp:
                    board[i][j] = temp.pop()
                else:
                    board[i][j] = 0



