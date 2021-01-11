# Largest Rectangle in Histogram - https://leetcode.com/problems/largest-rectangle-in-histogram/
'''Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
 '''

from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monotonicQueue = deque()
        largestRect = float('-inf')
        for i in range(len(heights)+1):
            currentHeight = heights[i] if i != len(heights) else 0
            while monotonicQueue and currentHeight < monotonicQueue[-1][1]: #Maintain a monotonic increasing sequence
                upperBound = monotonicQueue.pop()
                leftIndex = monotonicQueue[-1][0] if monotonicQueue else -1
                width = i - leftIndex - 1
                area = width * upperBound[1]
                largestRect = max(largestRect, area)
            monotonicQueue.append((i, currentHeight))
        return largestRect if largestRect != float('-inf') else 0