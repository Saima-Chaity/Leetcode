# Palindrome Number - https://leetcode.com/problems/palindrome-number/
'''Determine whether an integer is a palindrome. An integer is a palindrome when it
reads the same backward as forward.

Input: 121
Output: true'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        reverse = 0
        while x != 0:
            remainder = x % 10
            reverse = reverse*10 + remainder
            x //= 10
        return original == reverse