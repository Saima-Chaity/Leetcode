'''Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.'''

from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        mapping = defaultdict(list)
        for index, num in enumerate(nums):
            if num in mapping:
                mapping[num].append(index)
            else:
                mapping[num] = [index]

        pairsCount = 0
        for key, value in mapping.items():
            if len(value) > 1:
                i = 0
                while i < len(value):
                    remaining = value[i + 1:]
                    pairsCount += len(remaining)
                    i += 1
        return pairsCount


#Another approach
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        mapping = {}
        pairs = 0
        for num in nums:
            if num in mapping:
                pairs += mapping[num]
                mapping[num] += 1
            else:
                mapping[num] = 1
        return pairs


