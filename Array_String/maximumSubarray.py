# Maximum Subarray - https://leetcode.com/problems/maximum-subarray/
'''Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.'''

# Dynamic programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        return max(dp)


# Divide and conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(0, len(nums) - 1, nums)

    def helper(self, left, right, nums):
        if left == right:
            return nums[left]
        mid = left + (right - left) // 2
        leftSum = self.helper(left, mid, nums)
        rightSum = self.helper(mid + 1, right, nums)
        crossSum = self.cross_sum(left, right, mid, nums)
        return max(leftSum, rightSum, crossSum)

    def cross_sum(self, left, right, mid, nums):
        if left == right:
            return nums[left]
        leftSum = -float('inf')
        currSum = 0
        for i in range(mid, left - 1, -1):
            currSum += nums[i]
            leftSum = max(leftSum, currSum)

        rightSum = -float('inf')
        currSum = 0
        for i in range(mid + 1, right + 1):
            currSum += nums[i]
            rightSum = max(rightSum, currSum)
        return leftSum + rightSum

# Sliding window
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        result = float('-inf')
        for num in nums:
            current += num
            if current < num:
                current = num
            result = max(result, current)
        return result