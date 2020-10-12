# Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/
'''Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6

Input: [1,2,3,4]
Output: 24'''

# O(nlogn)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        result = max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])
        return result

# O(n)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        maxNumber1 = maxNumber2 = maxNumber3 = float('-inf')
        minNumber1 = minNumber2 = float('inf')
        
        for num in nums:
            if num > maxNumber1:
                maxNumber1, maxNumber2, maxNumber3 = num, maxNumber1, maxNumber2
            elif num > maxNumber2:
                maxNumber2, maxNumber3 = num, maxNumber2
            elif num > maxNumber3:
                maxNumber3 = num
            
            if num < minNumber1:
                minNumber1, minNumber2 = num, minNumber1
            elif num < minNumber2:
                minNumber2 = num
        
        # multiplying the three largest number;
        # multiplying the largest number with two negative numbers largest in magnitude.
        return max(maxNumber2 * maxNumber3, minNumber1 * minNumber2) * maxNumber1
    