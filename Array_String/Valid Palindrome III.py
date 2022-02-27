'''Valid Palindrome III - https://leetcode.com/problems/valid-palindrome-iii/

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
'''

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        def _isPalindrome(i, j, k):

            if k < 0:
                return False

            if j - i + 1 <= 1:  # string length <= 1
                return True

            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if s[i] == s[j]:
                memo[(i, j, k)] = _isPalindrome(i + 1, j - 1, k)
            else:
                memo[(i, j, k)] = _isPalindrome(i + 1, j, k - 1) or _isPalindrome(i, j - 1, k - 1)

            return memo[(i, j, k)]

        memo = {}
        return _isPalindrome(0, len(s) - 1, k)