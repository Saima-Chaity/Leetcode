# Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/
'''Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # Single scan. Given the current sum and the k, we check if (sum-k) existsed before at an earlier stage
        # (at a smaller window size). Keep expanding the sum while checking whether we have seen (sum - k) before

        mapping = {}
        mapping[0] = 1
        total = 0
        count = 0

        for num in nums:
            total += num
            if total - k in mapping:
                count += mapping[total - k]
            if total in mapping:
                mapping[total] += 1
            else:
                mapping[total] = 1
        return count
