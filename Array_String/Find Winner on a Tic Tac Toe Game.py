'''Find Winner on a Tic Tac Toe Game - https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of
the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw",
if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
'''


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        n = 3
        row = [0] * n
        col = [0] * n
        diagonal1 = 0
        diagonal2 = 0
        for index, move in enumerate(moves):
            value = 1 if index % 2 == 0 else -1
            row[move[0]] += value
            col[move[1]] += value
            if move[0] == move[1]:
                diagonal1 += value
            if move[1] == n - move[0] - 1:
                diagonal2 += value

            if abs(row[move[0]]) == n or abs(col[move[1]]) == n or abs(diagonal1) == n or abs(diagonal2) == n:
                return 'A' if index % 2 == 0 else 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
