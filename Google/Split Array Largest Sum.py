'''Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
'''


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def dfs(index, subArrayCount, currentSum, currentMax):
            if index == n and subArrayCount == m:
                self.output = min(currentMax, self.output)
                return

            if index == n:
                return

            if index > 0:
                dfs(index + 1, subArrayCount, currentSum + nums[index], max(currentMax, currentSum + nums[index]))

            if subArrayCount < m:
                dfs(index + 1, subArrayCount + 1, nums[index], max(currentMax, nums[index]))

        n = len(nums)
        self.output = float('inf')
        dfs(0, 0, 0, 0)
        return self.output


# Another approach
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        length = len(nums)
        dp = [[float('inf')] * (m + 1) for _ in range(length + 1)]
        dp[0][0] = 0
        prefixSum = [0] * (length + 1)
        for i in range(length):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        for i in range(1, length + 1):
            for j in range(1, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], prefixSum[i] - prefixSum[k]))
        return dp[length][m]

