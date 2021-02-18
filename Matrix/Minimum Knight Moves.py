'''Minimum Knight Moves - https://leetcode.com/problems/minimum-knight-moves/
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction,
then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
'''

# Time - O(|x|*|y|)
from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        direction = [(2, -1), (2, 1), (1, -2), (1, 2), (-2, -1), (-2, 1), (-1, -2), (1, -2), (-1, 2)]
        start_x = abs(x)
        start_y = abs(y)
        q = deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0))
        while q:
            x, y, steps = q.popleft()
            if (x, y) == (start_x, start_y):
                return steps
            for dx, dy in direction:
                next_x = x + dx
                next_y = y + dy
                if -1 <= next_x <= x + 2 and -1 <= next_y <= y + 2 and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    q.append((next_x, next_y, steps + 1))
        return -1
