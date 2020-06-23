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