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

        def backTrack(index, target, k, sum_so_far):
            visited_mapping = "".join(visited)
            if visited_mapping in memo:
                return memo[visited_mapping]
            if k == 0:
                return True
            if target == sum_so_far:
                memo[visited_mapping] = backTrack(0, target, k - 1, 0)
                return memo[visited_mapping]
            for i in range(index, len(nums)):
                if visited[i] == "0" and sum_so_far + nums[i] <= target:
                    visited[i] = "1"
                    if backTrack(i + 1, target, k, sum_so_far + nums[i]):
                        return True
                    visited[i] = "0"
            memo[visited_mapping] = False
            return memo[visited_mapping]

        total = sum(nums)
        max_num = max(nums)
        if total % k != 0 or max_num > total // k:
            return False

        visited = ["0"] * len(nums)
        memo = {}
        return backTrack(0, total // k, k, 0)