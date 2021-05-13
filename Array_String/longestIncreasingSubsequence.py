# Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/
'''Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. '''

# Time complexity: 0(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        maxLength = 1

        for i in range(1, len(dp)):
            maxValue = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxValue = max(maxValue, dp[j])
            dp[i] = maxValue + 1
            maxLength = max(maxLength, dp[i])
        return maxLength


# Using patience sort and binery search
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        def findIndex(nums, left, right, currentValue):
            while right - left > 1:
                mid = left + (right - left) // 2
                if nums[mid] >= currentValue:
                    right = mid
                else:
                    left = mid
            return right

        increasingTable = [0 for _ in range(len(nums) + 1)]
        length = 0
        increasingTable[0] = nums[0]
        length = 1

        for i in range(1, len(nums)):
            if nums[i] < increasingTable[0]:
                increasingTable[0] = nums[i]
            elif nums[i] > increasingTable[length - 1]:
                increasingTable[length] = nums[i]
                length += 1
            else:
                index = findIndex(increasingTable, -1, length - 1, nums[i])
                increasingTable[index] = nums[i]
        return length


#Reference: https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/