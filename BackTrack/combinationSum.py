# Combination Sum - https://leetcode.com/problems/combination-sum/
'''Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]'''

# BackTracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backTrack(index, combination, target):
            if target < 0:
                return
            if target == 0:
                output.append(combination)
                return
            for i in range(index, len(candidates)):
                backTrack(i, combination+[candidates[i]], target-candidates[i])
        
        candidates.sort()
        backTrack(0, [], target)
        return output

# BFS
from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        q = deque([(target, [], 0)])
        output = []
        while q:
            target, current, index = q.popleft()
            for i in range(index, len(candidates)):
                nextTarget = target - candidates[i]
                if nextTarget == 0:
                    output.append((current+[candidates[i]]))
                if nextTarget > 0:
                    q.append((nextTarget, current + [candidates[i]], i))
        return output


# Combination Sum II - https://leetcode.com/problems/combination-sum-ii/
'''Given a collection of candidate numbers (candidates) and a target number (target), find all unique 
combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backTrack(candidates, target, currentList, index):
            if target < 0:
                return
            if target == 0:
                output.append(currentList[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]: # Avoid duplicate
                    continue
                backTrack(candidates, target - candidates[i], currentList + [candidates[i]], i + 1) # next_index will be i+1 to Avoid duplicate
        output = []
        candidates.sort()
        backTrack(candidates, target, [], 0)
        return output


# BFS
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not target:
            return 0
        candidates.sort()
        q = deque([(0, [], 0)])
        output = []
        while q:
            total, path, index = q.popleft()
            if total == target:
                output.append(path)
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                nextValue = candidates[i] + total
                if nextValue <= target:
                    q.append((nextValue, path+[candidates[i]], i+1))
        return output


# Combination Sum III - https://leetcode.com/problems/combination-sum-iii/
'''Find all possible combinations of k numbers that add up to a number n, given that only numbers 
from 1 to 9 can be used and each combination should be a unique set of numbers.

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Input: k = 3, n = 7
Output: [[1,2,4]]'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backTrack(index, path, target):
            if len(path) > k:
                return
            if target < 0:
                return
            if target == 0 and len(path) == k:
                output.append(path)
                return
            for i in range(index, 10):
                backTrack(i + 1, path + [i], target - i)

        output = []
        backTrack(1, [], n)
        return output


# Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/
'''Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.'''

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def backTrack(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if target in mapping:
                return mapping[target]
            result = 0
            for i in range(len(nums)):
                result += backTrack(target - nums[i])
            mapping[target] = result
            return mapping[target]

        mapping = {}
        return backTrack(target)