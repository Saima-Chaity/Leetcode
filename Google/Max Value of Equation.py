'''Max Value of Equation - https://leetcode.com/problems/max-value-of-equation/

You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values,
where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get
3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values,
and give the value of 0 + 0 + |0 - 3| = 3.
'''

import heapq
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        if len(points) == 2:
            x0, y0 = points[0]
            x1, y1 = points[1]
            return y1 + y0 + x1 - x0

        heap = [(points[0][0] - points[0][1], points[0][0])]
        maxValue = float('-inf')

        for i in range(1, len(points)):
            xi, yi = points[i]

            while heap and xi - heap[0][1] > k:
                heapq.heappop(heap)

            if heap:
                difference, xj = heap[0][0], heap[0][1]
                maxValue = max(maxValue, yi + xi - difference)

            heapq.heappush(heap, (xi - yi, xi))
        return maxValue


# Using deque
from collections import deque
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        if len(points) == 2:
            x0, y0 = points[0]
            x1, y1 = points[1]
            return y1 + y0 + x1 - x0

        q = deque([(points[0][1] - points[0][0], points[0][0])])
        maxValue = float('-inf')

        for i in range(1, len(points)):
            xi, yi = points[i]

            # maintain the monotonicity (decreasing)
            while q and q[-1][0] <= yi - xi:
                difference, xj = q.pop()
                if xi - xj <= k:
                    maxValue = max(maxValue, yi + xi + difference)

            while q and xi - q[0][1] > k:
                q.popleft()

            if q:
                maxValue = max(maxValue, yi + xi + q[0][0])

            q.append((yi - xi, xi))

        return maxValue