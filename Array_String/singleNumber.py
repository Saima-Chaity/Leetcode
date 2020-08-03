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


# Single Number II - https://leetcode.com/problems/single-number-ii/
'''Given a non-empty array of integers, every element appears three times except for one, 
which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it 
without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3
Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for key, value in count.items():
            if value == 1:
                return key


# Single Number III - https://leetcode.com/problems/single-number-iii/
'''Given an array of numbers nums, in which exactly two elements appear only once and all 
the other elements appear exactly twice. Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        output = []
        for key, value in count.items():
            if value == 1:
                output.append(key)
        return output