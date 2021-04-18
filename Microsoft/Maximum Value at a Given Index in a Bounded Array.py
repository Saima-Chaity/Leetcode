'''Maximum Value at a Given Index in a Bounded Array -
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed)
that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
'''

'''Complexity Analysis:
Time:O(log(INT_MAX)) SPACE:O(1)'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def getSum(root, x):
            return x * root - (root * (root + 1) // 2)

        low = 1
        high = maxSum
        result = 0
        while low <= high:
            mid = low + (high - low) // 2
            left = getSum(min(mid - 1, index), mid)
            left += max(0, index - mid + 1)

            right = getSum(min(n - index - 1, mid - 1), mid)
            right += max(0, n - index - mid)

            if left + right + mid <= maxSum:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result

# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1120761/Greedy-%2B-BinarySearch-%2B-Math-%2B-Explained