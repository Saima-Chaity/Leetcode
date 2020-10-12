# Maximum Product Subarray - https://leetcode.com/problems/maximum-product-subarray/

'''Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.'''


# Brute force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProductValue = nums[0]
        for i in range(0, len(nums)):
            current = 1
            for j in range(i, len(nums)):
                current = current * nums[j]
                maxProductValue = max(maxProductValue, current)
        return maxProductValue

# DP
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums)):
            current = nums[i]
            temp = max(current, max_so_far * current, min_so_far * current)
            min_so_far = min(current, max_so_far * current, min_so_far * current) # using min_so_far for zero and negative values
            max_so_far = temp
            result = max(max_so_far, result)
        return result