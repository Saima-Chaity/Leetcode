'''Buildings With an Ocean View - https://leetcode.com/problems/buildings-with-an-ocean-view/

There are n buildings in a line. You are given an integer array heights of size n that represents
the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without
obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
'''

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        stack = []
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                stack.pop()
            stack.append(index)

        return stack


# O(1) space
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        result = []
        maxHeight = -1
        for i in range(len(heights) - 1, -1, -1):
            if maxHeight < heights[i]:
                result.append(i)
                maxHeight = heights[i]
        return result[::-1]