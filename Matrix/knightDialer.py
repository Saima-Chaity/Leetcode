# Knight Dialer - https://leetcode.com/problems/knight-dialer/
'''A chess knight can move as indicated in the chess diagram below:

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.
Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing
N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

Example 1:

Input: 1
Output: 10'''


class Solution:
    def knightDialer(self, N: int) -> int:
        # *   *   *   *   *   *   *   *
        # *   *   *   *   *   *   *   *
        # *   *   b   *   c   *   *   *
        # *   a   *   *   *   d   *   *
        # *   *   *   k   *   *   *   *
        # *   h   *   *   *   e   *   *
        # *   *   g   *   f   *   *   *
        # *   *   *   *   *   *   *   *

        self.maxValue = 10 ** 9 + 7
        summation = 0

        M = [[[0 for _ in range(3)] for _ in range(4)] for _ in range(N + 1)]
        for i in range(4):
            for j in range(3):
                summation = (summation + self.paths(M, i, j, N)) % self.maxValue
        return summation

    def paths(self, M, i, j, n):
        if i < 0 or j < 0 or i >= 4 or j >= 3 or (i == 3 and j != 1):
            return 0
        if n == 1:
            return 1
        if M[n][i][j] > 0:
            return M[n][i][j]

        M[n][i][j] = self.paths(M, i - 1, j - 2, n - 1) % self.maxValue + \
                     self.paths(M, i - 2, j - 1, n - 1) % self.maxValue + \
                     self.paths(M, i - 2, j + 1, n - 1) % self.maxValue + \
                     self.paths(M, i - 1, j + 2, n - 1) % self.maxValue + \
                     self.paths(M, i + 1, j + 2, n - 1) % self.maxValue + \
                     self.paths(M, i + 2, j + 1, n - 1) % self.maxValue + \
                     self.paths(M, i + 2, j - 1, n - 1) % self.maxValue + \
                     self.paths(M, i + 1, j - 2, n - 1) % self.maxValue
        return M[n][i][j]

# details: https://leetcode.com/problems/knight-dialer/discuss/190787/How-to-solve-this-problem-explained-for-noobs!!!