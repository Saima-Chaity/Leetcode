'''Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/
Given an array nums of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by k.

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
'''

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        mapping = {}
        mapping[0] = 1
        for i in range(len(nums)):
            total += nums[i]
            total = total % k
            count += mapping.get(total, 0)
            mapping[total] = mapping.get(total, 0) + 1
        return count