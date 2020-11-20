# Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/
'''Given a non-empty array nums containing only positive integers, find if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''


# Top Down Dynamic Programming - Memoization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(nums, index, targetSum):
            if targetSum == 0:
                return True
            if targetSum < 0 or index == 0:
                return False
            if targetSum in memo:
                return memo[targetSum]

            result = dfs(nums, index - 1, targetSum - nums[index - 1]) or dfs(nums, index - 1, targetSum)
            memo[targetSum] = result
            return result

        memo = {}
        total = sum(nums)
        if total % 2 != 0:
            return False
        return dfs(nums, len(nums), total // 2)


# Bottom Up Dynamic Programming
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        n = len(nums)
        dp = [[False for _ in range((total // 2) + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            current = nums[i - 1]
            for j in range(0, total // 2 + 1):
                if j < current:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - current]
        return dp[n][total // 2]
