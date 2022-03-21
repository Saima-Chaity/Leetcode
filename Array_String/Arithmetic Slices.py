'''Arithmetic Slices - https://leetcode.com/problems/arithmetic-slices/

An integer array is called arithmetic if it consists of at least three elements and if the difference between
any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
'''


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return 0

        result = 0
        for i in range(len(nums) - 2):
            diff = nums[i + 1] - nums[i]
            for j in range(i + 2, len(nums)):
                if nums[j] - nums[j - 1] == diff:
                    result += 1
                else:
                    break
        return result