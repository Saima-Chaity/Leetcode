# Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/
'''Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0
        for num in numSet:
            if num - 1 not in numSet:  # That means it is the first element in the sequence
                currentNumber = num
                currentLength = 1
                while currentNumber + 1 in numSet:
                    currentNumber += 1
                    currentLength += 1
                longestSequence = max(longestSequence, currentLength)
        return longestSequence
