# N-Queens - https://leetcode.com/problems/n-queens/
'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens
attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def createBoard(board, visited):
            for r, c in visited:
                current = list(board[r])
                current[c] = "Q"
                board[r] = "".join(current)
            return board

        def underAttack(row, col):
            for r, c in visited:
                if r == row or c == col or abs(r - row) == abs(c - col):
                    return True
            return False

        def backTrack(row):
            for col in range(n):
                if not underAttack(row, col):
                    visited.add((row, col))
                    if row == n - 1:
                        board = ["." * n for _ in range(n)]
                        output.append(createBoard(board, visited))
                    else:
                        backTrack(row + 1)
                    visited.remove((row, col))

        visited = set()
        output = []
        backTrack(0)
        return output


# N-Queens II - https://leetcode.com/problems/n-queens-ii/
'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two 
queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
'''

class Solution:
    def totalNQueens(self, n: int) -> int:

        def underAttack(row, col):
            for r, c in visited:
                if r == row or c == col or abs(r - row) == abs(c - col):
                    return True
            return False

        def backTrack(row, count):
            for col in range(n):
                if not underAttack(row, col):
                    visited.add((row, col))
                    if row == n - 1:
                        count += 1
                    else:
                        count = backTrack(row + 1, count)
                    visited.remove((row, col))
            return count

        visited = set()
        return backTrack(0, 0)