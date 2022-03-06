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
        end = len(nums) - 1
        lastIndex = end
        result = [0] * len(nums)
        while start <= end:
            start_square = nums[start] * nums[start]
            end_square = nums[end] * nums[end]
            if start_square > end_square:
                result[lastIndex] = start_square
                start += 1
            else:
                result[lastIndex] = end_square
                end -= 1
            lastIndex -= 1
        return result