# Subsets - https://leetcode.com/problems/subsets/
'''Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        def backTrack(index, path):
            if index > 0 and index <= len(nums) and path not in output:
                output.append(path)
            
            for i in range(index, len(nums)):
                backTrack(i+1, path+[nums[i]])
            
        backTrack(0, [])
        return output


# Subsets II - https://leetcode.com/problems/subsets-ii/
'''Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        nums.sort()
        def backTrack(index, path):
            if path:
                output.append(path)
                
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                backTrack(i+1, path+[nums[i]])
            
        backTrack(0, [])
        return output