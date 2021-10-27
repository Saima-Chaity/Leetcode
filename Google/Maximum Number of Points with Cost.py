'''Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize
the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c)
will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row.
For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1)
and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.

Example 1:

Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
'''


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def getLeftToRightPoint(points):
            currentRow = [points[0]] + [0] * (len(points) - 1)
            for i in range(1, len(points)):
                currentRow[i] = max(currentRow[i - 1] - 1, points[i])
            return currentRow

        def getRightToLeftPoints(points):
            currentRow = [0] * (len(points) - 1) + [points[-1]]
            for i in range(len(points) - 2, -1, -1):
                currentRow[i] = max(currentRow[i + 1] - 1, points[i])
            return currentRow

        for i in range(1, len(points)):
            leftToRight, rightToLeft = getLeftToRightPoint(points[i - 1]), getRightToLeftPoints(points[i - 1])
            for j in range(len(points[0])):
                points[i][j] = max(leftToRight[j], rightToLeft[j]) + points[i][j]
        return max(points[-1])
