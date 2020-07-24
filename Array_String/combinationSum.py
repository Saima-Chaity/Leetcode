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

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {}
        for candidate in candidates:
            for i in range(candidate, target + 1):
                if i == candidate:
                    if i not in dp:
                        dp[i] = [[candidate]]
                    else:
                        dp[i] += [[candidate]]
                else:
                    if i - candidate > 0 and i - candidate in dp:
                        for numSet in dp[i - candidate]:
                            x = numSet + [candidate]
                            if i not in dp:
                                dp[i] = [x]
                            else:
                                dp[i].append(x)
        if target not in dp:
            return []
        return dp[target]

# BackTracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backTrack(candidates, target, currentList, index):
            if target < 0:
                return
            if target == 0:
                output.append(currentList[:])
                return
            for i in range(index, len(candidates)):
                backTrack(candidates, target - candidates[i], currentList + [candidates[i]], i)
        output = []
        candidates.sort()
        backTrack(candidates, target, [], 0)
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
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                backTrack(candidates, target - candidates[i], currentList + [candidates[i]], i + 1)
        output = []
        candidates.sort()
        backTrack(candidates, target, [], 0)
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

        def backTrack(K, target, currentList, index):
            if K == 0 and target == 0:
                output.append(currentList[:])
                return
            for i in range(index, 10):
                backTrack(K - 1, target - i, currentList + [i], i + 1)
        output = []
        backTrack(k, n, [], 1)
        return output

