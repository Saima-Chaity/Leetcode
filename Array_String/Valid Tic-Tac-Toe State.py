'''Valid Tic-Tac-Toe State - https://leetcode.com/problems/valid-tic-tac-toe-state/

Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this
board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Example 1:

Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
'''


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        n = len(board)
        rows = [[0, 0] for _ in range(n)]
        cols = [[0, 0] for _ in range(n)]
        diagonalAscending = [0, 0]
        diagonalDescending = [0, 0]
        moves = [0, 0]
        win = -1
        for row in range(3):
            for col, move in enumerate(board[row]):
                if move == " ":
                    continue

                player = 0
                if move == "O":
                    player = 1
                rows[row][player] += 1
                cols[col][player] += 1
                if row == col:
                    diagonalAscending[player] += 1
                if col == n - row - 1:
                    diagonalDescending[player] += 1

                moves[player] += 1
                if rows[row][player] == 3 or cols[col][player] == 3 or diagonalAscending[player] == 3 or \
                        diagonalDescending[player] == 3:
                    if win > -1 and win != player:
                        return False
                    win = player

        if moves[1] > moves[0] or abs(moves[1] - moves[0]) > 1:
            return False
        if win == 0 and moves[0] <= moves[1]:
            return False
        if win == 1 and moves[0] > moves[1]:
            return False
        return True

