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
        trie = {}
        for word in words:
            t = trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t["#"] = "#"

        row = len(board)
        col = len(board[0])
        self.output = set()

        for i in range(row):
            for j in range(col):
                self.checkNeighbor(i, j, board, trie, "")
        return self.output

    def checkNeighbor(self, i, j, board, trie, path):
        if "#" in trie:
            self.output.add(path)
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] not in trie:
            return
        temp = board[i][j]
        board[i][j] = "@"
        self.checkNeighbor(i + 1, j, board, trie[temp], path + temp)
        self.checkNeighbor(i - 1, j, board, trie[temp], path + temp)
        self.checkNeighbor(i, j + 1, board, trie[temp], path + temp)
        self.checkNeighbor(i, j - 1, board, trie[temp], path + temp)
        board[i][j] = temp


# Modified previous solution
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def dfs(x, y, trie, path):
            if "#" in trie:
                output.add(path)

            for dx, dy in directions:
                xi = x + dx
                yj = y + dy
                if 0 <= xi < rows and 0 <= yj < cols and board[xi][yj] != "@" and board[xi][yj] in trie:
                    temp = board[xi][yj]
                    board[xi][yj] = '@'
                    dfs(xi, yj, trie[temp], path + temp)
                    board[xi][yj] = temp

        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        output = set()
        trie = {}

        for word in words:
            t = trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t["#"] = "#"

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    temp = board[i][j]
                    board[i][j] = '@'
                    dfs(i, j, trie[temp], temp)
                    board[i][j] = temp
        return output