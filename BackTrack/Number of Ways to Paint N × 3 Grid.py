'''Number of Ways to Paint N × 3 Grid - https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors:
Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that
share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow
large, the answer must be computed modulo 109 + 7.

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
'''


class Solution:
    def numOfWays(self, n: int) -> int:

        @lru_cache(None)
        def getCounts(index, color1, color2, color3):
            if index == n:
                return 1

            nc1, nc2, nc3 = 0, 0, 0
            answer = 0
            for i in range(1, 4):
                if i != color1:
                    nc1 = i
                    for j in range(1, 4):
                        if j != color2 and j != nc1:
                            nc2 = j
                            for k in range(1, 4):
                                if k != color3 and k != nc2:
                                    nc3 = k
                                    answer += getCounts(index + 1, nc1, nc2, nc3)

            return answer % mod

        mod = 10 ** 9 + 7
        return getCounts(0, 0, 0, 0)
