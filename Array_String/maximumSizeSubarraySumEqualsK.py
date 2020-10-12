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
        mapping = collections.defaultdict(int)
        sum_so_far = 0
        result = float('-inf')
        for index, num in enumerate(nums):
            sum_so_far += num
            if sum_so_far not in mapping:
                mapping[sum_so_far] = index
            
            if sum_so_far == k:
                result = max(result, index - 0 + 1) #everything from 0, to i has been aggregated to add up to k. Length = i-0+1
            
            #The idea is that if there is a number in a map where sum less k equals to a number already in a table, there must be a contiguous section from that point (mp[acc - k]) to current point (i) where the sum of all items is k.
            elif sum_so_far - k in mapping:
                result = max(result, index - mapping[sum_so_far - k])
        return result if result != float('-inf') else 0