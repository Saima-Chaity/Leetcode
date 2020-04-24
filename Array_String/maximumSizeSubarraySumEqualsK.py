# Maximum Size Subarray Sum Equals k - https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
'''Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one,
return 0 instead.
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.'''


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        maxLength = 0
        mapping = {}
        sumSoFar = 0

        for i in range(len(nums)):
            sumSoFar += nums[i]
            if sumSoFar == k:
                maxLength = i + 1
            elif (sumSoFar - k) in mapping:
                maxLength = max(maxLength, i - mapping[sumSoFar - k])
            if sumSoFar not in mapping:
                mapping[sumSoFar] = i
        return maxLength