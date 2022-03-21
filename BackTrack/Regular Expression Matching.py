# Regular Expression Matching - https://leetcode.com/problems/regular-expression-matching/
'''Given an input string (s) and a pattern (p), implement regular expression matching 
with support for '.' and '*' where: 

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by 
repeating 'a' once, it becomes "aa".'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        '''case 1: p == *, then check if the second last char of p matches with s or second last char of p == .
            if it is true, remove one char from s and check again or remove two char from p

        case 2: if  p matches with s or  p == .
            remove one char from s and remove one char from p
        '''

        class Solution:
            def isMatch(self, s: str, p: str) -> bool:

                def _isMatch(s, p):
                    if (s, p) in memo:
                        return memo[(s, p)]
                    if s == p:
                        memo[(s, p)] = True
                    elif s and not p:
                        memo[(s, p)] = False
                    elif p[-1] == "*":
                        if s and (s[-1] == p[-2] or p[-2] == "."):
                            memo[(s, p)] = _isMatch(s[:-1], p) or _isMatch(s, p[:-2])
                        else:
                            memo[(s, p)] = _isMatch(s, p[:-2])
                    elif s and (s[-1] == p[-1] or p[-1] == "."):
                        memo[(s, p)] = _isMatch(s[:-1], p[:-1])
                    else:
                        memo[(s, p)] = False
                    return memo[(s, p)]

                memo = {}
                return _isMatch(s, p)