# Valid Palindrome - https://leetcode.com/problems/valid-palindrome/
'''Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true'''


class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphanumericStr = ""
        for char in s:
            if char.isalnum():
                alphanumericStr += char.lower()
        return alphanumericStr == alphanumericStr[::-1]

# 0(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


# Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/
'''Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] != s[right]:
                s_Left = s[:left] + s[left + 1:]
                s_Right = s[:right] + s[right + 1:]
                return s_Left == s_Left[::-1] or s_Right == s_Right[::-1]
        return True



