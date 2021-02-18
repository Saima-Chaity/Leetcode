'''Alphabet Board Path - https://leetcode.com/problems/alphabet-board-path/

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.
You may return any path that does so.

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"'''

from collections import deque
class Solution:
    def alphabetBoardPath(self, target: str) -> str:

        def bfs(x, y, char):
            if board[x][y] == char:
                return x, y, "!"
            q = deque([(x, y, "")])
            visited = set()
            visited.add((x, y))
            while q:
                x, y, path = q.popleft()
                for dx, dy, dr in direction:
                    next_x = x + dx
                    next_y = y + dy
                    if 0 <= next_x < row and 0 <= next_y < len(board[next_x]) and (next_x, next_y) not in visited:
                        if char == board[next_x][next_y]:
                            path += dr + "!"
                            return next_x, next_y, path
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y, path + dr))

        result = []
        direction = [(0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U')]
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        row = len(board)
        x = 0
        y = 0
        for char in target:
            x, y, path = bfs(x, y, char)
            result.append(path)
        return "".join(result)
