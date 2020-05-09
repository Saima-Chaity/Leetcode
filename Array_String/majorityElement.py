# Majority Element - https://leetcode.com/problems/majority-element/
'''Given an array of size n, find the majority element. The majority element is the element that appears
more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        lengthOfNums = len(nums)
        requiredAppearance = lengthOfNums // 2
        mapping = collections.Counter(nums)

        for key, value in mapping.items():
            if value > requiredAppearance:
                return key


# Majority Element II - https://leetcode.com/problems/majority-element-ii/
'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lengthOfNums = len(nums)
        requiredAppearance = lengthOfNums // 3
        mapping = collections.Counter(nums)

        i = 0
        for key, value in mapping.items():
            if value > requiredAppearance:
                nums[i] = key
                i += 1
        return nums[:i]