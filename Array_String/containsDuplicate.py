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

# Contains Duplicate II - https://leetcode.com/problems/contains-duplicate-ii/
'''Given an array of integers and an integer k, find out whether there are two distinct 
indices i and j in the array such that nums[i] = nums[j] and the absolute difference 
between i and j is at most k.

Input: nums = [1,2,3,1], k = 3
Output: true'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for index, num in enumerate(nums):
            if num in mapping:
                if abs(mapping[num] - index) <= k:
                    return True
            mapping[num] = index
        return False

# Contains Duplicate III - https://leetcode.com/problems/contains-duplicate-iii/
'''Given an array of integers, find out whether there are two distinct indices i and j in 
the array such that the absolute difference between nums[i] and nums[j] is at most t and the 
absolute difference between i and j is at most k.
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        def getDifference(left, right):
            return abs(sorted_nums[left][1] - sorted_nums[right][1]), \
                   abs(sorted_nums[left][0] - sorted_nums[right][0])

        # Sort by value
        sorted_nums = [x for x in sorted(enumerate(nums), key=lambda x: x[1])]
        left = 0
        for right in range(1, len(nums)):
            differenceValue, differenceIndex = getDifference(left, right)
            while left < right - 1 and differenceValue > t:
                left += 1
            differenceValue, differenceIndex = getDifference(left, right)
            if differenceValue <= t and differenceIndex <= k:
                return True
        return False
