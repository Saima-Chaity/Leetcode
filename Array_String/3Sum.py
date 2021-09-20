# 3Sum - https://leetcode.com/problems/3sum/
'''Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique 
triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.findTwoSum(nums, 0, i)
        return self.results
    
    def findTwoSum(self, nums, target, i):
        left = i + 1
        right = len(nums)-1
        
        while left < right:
            total = nums[left] + nums[right] + nums[i]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                self.results.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
                


# 3Sum Smaller - https://leetcode.com/problems/3sum-smaller/
'''Given an array of n integers nums and an integer target, find the number of index triplets i, j, k 
with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?
Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]'''

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        count = 0
        nums.sort()
        for i in range(0, len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    count += right-left
                    left += 1
                else:
                    right -= 1
        return count



# 3Sum Closest - https://leetcode.com/problems/3sum-closest/
'''Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        output = 0
        closet = float('inf')
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                diff = abs(target - total)
                if diff == 0:
                    return total
                if diff < closet:
                    closet = diff
                    output = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return output