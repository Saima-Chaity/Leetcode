# Word Search - https://leetcode.com/problems/word-search/
'''Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        def dfs(i, j, currentIndex, board):
            if currentIndex == len(word):
                return True

            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != word[currentIndex]:
                return False
            temp = board[i][j]
            board[i][j] = '@'
            result = dfs(i + 1, j, currentIndex + 1, board) or \
                     dfs(i - 1, j, currentIndex + 1, board) or \
                     dfs(i, j - 1, currentIndex + 1, board) or \
                     dfs(i, j + 1, currentIndex + 1, board)
            board[i][j] = temp
            return result

        row = len(board)
        col = len(board[0])
        startIndex = 0

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[startIndex]:
                    result = dfs(i, j, startIndex, board)
                    if result:
                        return True
        return False
