# Permutations - https://leetcode.com/problems/permutations/
'''Given a collection of distinct integers, return all possible permutations.
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backTrack(first = 0):
            if first == numLength:
                output.append(nums[:])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backTrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        numLength  = len(nums)
        backTrack()
        return output

# Permutations II - https://leetcode.com/problems/permutations-ii/
'''Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backTrack(nums, path, visited):
            if len(path) == len(nums):
                output.append(path[:])
                return
            for i in range(0, len(nums)):
                if not visited[i]:
                    if i > 0 and not visited[i-1] and nums[i] == nums[i-1]:
                        continue
                    else:
                        visited[i] = True
                        backTrack(nums, path+[nums[i]], visited)
                        visited[i] = False
        output = []
        nums.sort()
        visited = [False] * len(nums)
        backTrack(nums, [], visited)
        return output