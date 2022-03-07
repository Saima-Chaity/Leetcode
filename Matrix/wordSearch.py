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


# Word Search II - https://leetcode.com/problems/word-search-ii/
'''Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally 
or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]'''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.trie = {}
        for word in words:
            t = self.trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t["#"] = word

        self.direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.output = []
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in self.trie:
                    self.dfs(i, j, self.trie)
        return self.output

    def dfs(self, i, j, trie):

        temp = self.board[i][j]
        current = trie[temp]
        word_match = current.pop("#", False)
        if word_match:
            self.output.append(word_match)

        self.board[i][j] = "@"
        for dx, dy in self.direction:
            x = i + dx
            y = j + dy
            if 0 <= x < self.row and 0 <= y < self.col and self.board[x][y] != "@" and self.board[x][y] in current:
                self.dfs(x, y, current)

        self.board[i][j] = temp
        if not current:
            trie.pop(temp)