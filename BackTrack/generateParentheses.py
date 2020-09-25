# Generate Parentheses - https://leetcode.com/problems/generate-parentheses/
'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backTrack(S="", left=0, right=0):
            if len(S) == 2 * n:
                result.append(S)
                return
            if left < n:
                backTrack(S + '(', left + 1, right)
            if right < left:
                backTrack(S + ')', left, right + 1)
        backTrack()
        return result