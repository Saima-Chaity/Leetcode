# Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/
'''Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the
product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [0] * len(nums)
        result[0] = 1
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * right
            right *= nums[i]

        return result
