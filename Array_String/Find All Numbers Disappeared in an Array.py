# Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        output = []
        numSet = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in numSet:
                output.append(i)
        return output


#O(1) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        output = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1

        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                output.append(i)
        return output