# Missing Number - https://leetcode.com/problems/missing-number/
'''Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2'''

#Using sorting
class Solution:
    def missingNumber(self, nums):

        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)

        elif nums[0] != 0:
            return 0

        for i in range(1, len(nums)):
            nextNumber = nums[i - 1] + 1
            if nums[i] != nextNumber:
                return nextNumber


#Using HashSet
class Solution:
    def missingNumber(self, nums):

        numSet = set(nums)
        for index in range(len(nums) + 1):
            if index not in numSet:
                return index