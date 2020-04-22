# Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/
'''Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3'''

# Brute Force
class NumArray:

    def __init__(self, nums: List[int]):
        self.numsArr = nums

    def sumRange(self, i: int, j: int) -> int:
        totalSum = 0
        for i in range(i, j + 1):
            totalSum += self.numsArr[i]
        return totalSum


# NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# Caching
class NumArray(object):
    def __init__(self, nums):
        """
        initialize data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums:
            self.accu += self.accu[-1] + num,

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j + 1] - self.accu[i]

# NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)