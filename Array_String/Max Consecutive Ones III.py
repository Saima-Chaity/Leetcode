'''Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if
you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1