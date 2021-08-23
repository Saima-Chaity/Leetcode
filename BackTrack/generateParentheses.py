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


'''The way I like to think about the runtime of backtracking algorithms is O(b^d), where b is the 
branching factor and d is the maximum depth of recursion.

Backtracking is characterized by a number of decisions b that can be made at each level of recursion. 
If you visualize the recursion tree, this is the number of children each internal node has. You can 
also think of b as standing for "base", which can help you remember that b is the base of the exponential.

If we can make b decisions at each level of recursion, and we expand the recursion tree to d levels 
(ie: each path has a length of d), then we get b^d nodes. Since backtracking is exhaustive and must 
visit each one of these nodes, the runtime is O(b^d).'''
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