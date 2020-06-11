# Single Number - https://leetcode.com/problems/single-number/
'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Example 1:

Input: [2,2,1]
Output: 1'''

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        mapping = Counter(nums)

        for key, value in mapping.items():
            if value == 1:
                return key


