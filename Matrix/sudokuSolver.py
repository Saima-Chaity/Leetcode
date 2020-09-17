# Sudoku Solver - https://leetcode.com/problems/sudoku-solver/
'''Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.'''

from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        row = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                value = int(board[i][j])
                row[i].add(value)
                col[j].add(value)
                boxes[(i//3) * 3 + j//3].add(value)
        
        def isValid(r, c, value):
            box_id = (r // 3) * 3 + c // 3
            return value not in row[r] and value not in col[c] and value not in boxes[box_id]
        
        def backTrack(r, c):
            if r == n-1 and c == n:
                return True
            elif c == n:
                c = 0
                r += 1
            
            if board[r][c] != ".":
                return backTrack(r, c+1)
            
            box_id = (r // 3) * 3 + c // 3
            for value in range(1, n+1):
                if not isValid(r, c, value):
                    continue
                
                board[r][c] = str(value)
                row[r].add(value)
                col[c].add(value)
                boxes[box_id].add(value)
                
                if backTrack(r, c+1):
                    return True
                
                board[r][c] = "."
                row[r].remove(value)
                col[c].remove(value)
                boxes[box_id].remove(value)
            return False
        
        backTrack(0, 0)
            