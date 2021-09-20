# 4Sum - https://leetcode.com/problems/4sum/
'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]'''


# N - sum where N >= 2 solution:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)

    def kSum(self, nums, target, k):
        results = []
        if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
            return results

        if k == 2:
            return self.findTwoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for path in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    results.append([nums[i]] + path)
        return results

    def findTwoSum(self, nums, target):
        results = []
        left = 0
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                results.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
        return results


# Using three sum
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def getSum(i, j):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            return result

        nums.sort()
        result = []
        for i in range(0, len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums)):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        getSum(i, j)
        return result



# 4Sum II - https://leetcode.com/problems/4sum-ii/
'''Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the 
number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 
Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1'''


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        count = 0
        mapping = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                mapping[nums1[i] + nums2[j]] = mapping.get(nums1[i] + nums2[j], 0) + 1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                count += mapping.get(-(nums3[i] + nums4[j]), 0)

        return count