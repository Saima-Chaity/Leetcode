# Valid Sudoku - https://leetcode.com/problems/valid-sudoku/
'''Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                box_id = (i//3) * 3 + j//3
                row[i][num] = row[i].get(num, 0) + 1
                col[j][num] = col[j].get(num, 0) + 1
                boxes[box_id][num] = boxes[box_id].get(num, 0) + 1

                if row[i][num] > 1 or col[j][num] > 1 or boxes[box_id][num] > 1:
                    return False
        return True
                