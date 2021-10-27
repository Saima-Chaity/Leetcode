'''Number of Subarrays with Bounded Maximum
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

Given an integer array nums and two integers left and right, return the number of contiguous non-empty
subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
'''


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:

        def count(bound):
            result = current = 0
            for i in range(len(nums)):
                if nums[i] <= bound:
                    current += 1
                else:
                    current = 0
                result += current
            return result

        return count(right) - count(left - 1)