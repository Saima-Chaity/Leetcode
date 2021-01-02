# Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]'''

from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mapping = Counter(nums)
        return [num for num, freq in mapping.items() if freq > 1]

#O(1) space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        output = []
        for i in range(len(nums)):
            num = abs(nums[i]) - 1
            if nums[num] > 0:
                nums[num] *= -1
            else:
                output.append(num + 1)
        return output
