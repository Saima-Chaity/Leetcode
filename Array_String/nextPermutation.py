# Next Permutation - https://leetcode.com/problems/next-permutation/
'''Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start):
            i = start
            j = len(nums) - 1

            while i < j:
                swap(nums, i, j)
                i += 1
                j -= 1

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]: # Find first decreasing number
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]: # Find increasing number greater than number at i
                j -= 1
            swap(nums, i, j)
        reverse(nums, i + 1)