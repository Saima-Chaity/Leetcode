'''Wildcard Matching - https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def removeStar(p):
            p = list(p)
            for i in range(1, len(p)):
                if p[i - 1] == p[i] == "*":
                    p[i - 1] = ""
            return "".join(p)

        def helper(s, p):
            if (s, p) in memo:
                return memo[(s, p)]

            if p == s or p == "*":
                memo[(s, p)] = True

            elif not s or not p:
                memo[(s, p)] = False

            elif p[0] == s[0] or p[0] == "?":
                memo[(s, p)] = helper(s[1:], p[1:])
            elif p[0] == "*":
                memo[(s, p)] = helper(s[1:], p) or helper(s, p[1:])
            else:
                memo[(s, p)] = False
            return memo[(s, p)]

        p = removeStar(p)
        memo = {}
        return helper(s, p)
