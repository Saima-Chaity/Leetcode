# Contains Duplicate - https://leetcode.com/problems/contains-duplicate/
'''Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Input: [1,2,3,1]
Output: true'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for index, num in enumerate(nums):
            if num not in mapping:
                mapping[num] = index
            else:
                return True
        return False