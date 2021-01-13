# Squares of a Sorted Array - https://leetcode.com/problems/squares-of-a-sorted-array/
'''Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        start = 0
        end = len(nums)-1
        i = end
        output = [0] * (end+1)
        while start <= end:
            startNumber = nums[start] * nums[start]
            endNumber = nums[end] * nums[end]
            if startNumber > endNumber:
                output[i] = startNumber
                i -= 1
                start += 1
            else:
                output[i] = endNumber
                i -= 1
                end -= 1
        return output