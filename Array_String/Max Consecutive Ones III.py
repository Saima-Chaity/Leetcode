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


# Another approach
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        left = 0
        maxLength = -1
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1

            while left <= i and zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maxLength = max(maxLength, i - left + 1)
        return maxLength