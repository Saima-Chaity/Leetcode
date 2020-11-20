# Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''Given an array of integers nums and a positive integer k, find whether it's possible
to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def dfs(index, currentSum, k):
            if k == 0:
                return True

            if currentSum == targetSum:
                return dfs(0, 0, k - 1)

            for i in range(index, len(nums)):
                if not visited[i] and currentSum + nums[i] <= targetSum:
                    visited[i] = True
                    if dfs(i + 1, currentSum + nums[i], k):
                        return True
                    visited[i] = False
            return False

        total = 0
        maxNumber = -1
        for i in range(len(nums)):
            total += nums[i]
            maxNumber = max(maxNumber, nums[i])

        if total % k != 0 or maxNumber > total // k:
            return False

        targetSum = total // k
        visited = [False] * len(nums)
        return dfs(0, 0, k)
