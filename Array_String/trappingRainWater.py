# Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/
'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6'''


class Solution:
    def trap(self, height: List[int]) -> int:

        '''we can see height[left] < height[right],then for pointerleft, he knows a taller bar exists on his right side,
        then if leftMax is taller than him, he can contain some water for sure(in our case).
        So we go ans += (left_max - height[left]). But if leftMax is shorter than him, then there isn't a left side bar can
        help him contain water, then he will become other bars' leftMax. so execute (left_max = height[left]).
        '''

        leftMax = 0
        rightMax = 0
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            if height[left] < height[right]:
                if leftMax > height[left]:
                    result += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if rightMax > height[right]:
                    result += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return result


#Using stack
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        waterTrapped = 0
        for index, currentHeight in enumerate(height):
            # Form a container
            while stack and stack[-1][0] <= currentHeight:
                popped, currentIndex = stack.pop()
                # If container, then calculate left boundary
                if stack:
                    leftBoundary, leftIndex = stack[-1]
                    waterTrapped += min(leftBoundary-popped, currentHeight-popped) * (index - leftIndex - 1)
            stack.append((currentHeight, index))
        return waterTrapped









