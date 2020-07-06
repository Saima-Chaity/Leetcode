# Combinations - https://leetcode.com/problems/combinations/
'''Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backTrack(currentNumber, path):
            if len(path) == k:
                output.append(path[:])
                return
            for i in range(currentNumber, n+1):
                path.append(i)
                backTrack(i+1, path)
                path.pop()
        backTrack(1, [])
        return output