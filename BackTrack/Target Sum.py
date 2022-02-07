'''Target Sum - https://leetcode.com/problems/target-sum/

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each
integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them
to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
'''


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def targetSum(index, sum_so_far):
            if index == len(nums) and sum_so_far == target:
                return 1
            if index >= len(nums):
                return 0
            if (index, sum_so_far) in memo:
                return memo[(index, sum_so_far)]

            addition = targetSum(index + 1, sum_so_far + nums[index])
            substract = targetSum(index + 1, sum_so_far - nums[index])
            memo[(index, sum_so_far)] = addition + substract
            return memo[(index, sum_so_far)]

        memo = {}
        return targetSum(0, 0)