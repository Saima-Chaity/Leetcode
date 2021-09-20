'''Maximize Score After N Operations - https://leetcode.com/problems/maximize-score-after-n-operations/

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
'''


class Solution:
    def maxScore(self, nums: List[int]) -> int:

        def gcd(a, b):
            return b if (a % b) == 0 else gcd(b, a % b)

        def backTrack(nums, index):
            if index == length:
                return 0

            if (nums, index) not in memo:
                array, memo[(nums, index)] = list(nums), 0
                for i in range(len(nums) - 1):
                    for j in range(i + 1, len(nums)):
                        newArray = array[:i] + array[i + 1:j] + array[j + 1:]
                        result = (index + 1) * gcd(array[i], array[j])
                        memo[(nums, index)] = max(memo[(nums, index)], result + backTrack(tuple(newArray), index + 1))
            return memo[(nums, index)]

        memo = {}
        length = len(nums) // 2 + 1
        return backTrack(tuple(nums), 0)
