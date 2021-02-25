'''First Missing Positive - https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
'''

from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        numsLength = len(nums)
        if 1 not in nums:
            return 1

        if numsLength == 1:
            return 2

        # Remove negative and zero values
        for i in range(numsLength):
            if nums[i] <= 0 or nums[i] > numsLength:
                nums[i] = 1

        mapping = Counter(nums)
        smallest = float('inf')
        for key, value in mapping.items():
            if key + 1 not in mapping:
                smallest = min(smallest, key + 1)
        return smallest


# Constant space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        numsLength = len(nums)
        if 1 not in nums:
            return 1

        if numsLength == 1:
            return 2

        # Remove negative and zero values
        for i in range(numsLength):
            if nums[i] <= 0 or nums[i] > numsLength:
                nums[i] = 1

        # If we find a number in nums list change the value at the number index
        for i in range(numsLength):
            current = abs(nums[i])
            if current == numsLength:
                nums[0] = - abs(nums[0])
                continue
            else:
                nums[current] = - abs(nums[current])

        for i in range(1, numsLength):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return numsLength

        return numsLength + 1

