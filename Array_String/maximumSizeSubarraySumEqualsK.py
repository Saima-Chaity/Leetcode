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

        largest = 0
        sum_so_far = 0
        mapping = {}
        for i in range(len(nums)):
            sum_so_far += nums[i]
            if sum_so_far == k:
                largest = i + 1
            if sum_so_far - k in mapping:
                largest = max(largest, i - mapping[sum_so_far - k])
            if sum_so_far not in mapping:
                mapping[sum_so_far] = i
        return largest