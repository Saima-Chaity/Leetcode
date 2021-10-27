'''Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

Given an array nums and an integer target.

Return the maximum number of non-empty non-overlapping subarrays such that the sum of values in
each subarray is equal to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
'''


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:

        mapping = {}
        mapping[0] = -1
        nextIndex = -1
        count = 0
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - target in mapping and mapping[prefixSum - target] >= nextIndex:
                count += 1
                nextIndex = i
            mapping[prefixSum] = i
        return count