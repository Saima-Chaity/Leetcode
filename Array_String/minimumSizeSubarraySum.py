# Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/
'''Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous
subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        if not nums:
            return 0

        left = 0
        sum_so_far = 0
        minSum = float('inf')

        for i in range(len(nums)):
            sum_so_far += nums[i]
            while sum_so_far >= s:
                minSum = min(minSum, i - left + 1)
                sum_so_far -= nums[left]
                left += 1
        return minSum if (minSum != float('inf')) else 0

