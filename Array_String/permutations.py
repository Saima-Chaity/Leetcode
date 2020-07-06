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