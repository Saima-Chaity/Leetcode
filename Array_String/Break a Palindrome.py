# Break a Palindrome - https://leetcode.com/problems/break-a-palindrome/
'''Given a palindromic string palindrome, replace exactly one character by any lowercase English
letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Example 2:

Input: palindrome = "a"
Output: ""
'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        '''Check half of the string,
            replace a non 'a' character to 'a'.

            If only one character, return empty string.
            Otherwise repalce the last character to 'b'
        '''

        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        return palindrome[:-1] + "b" if palindrome[:-1] else ""


# Another solution
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]

        palindrome = list(palindrome)
        lowestIndexFound = False
        for i in range(len(palindrome)):
            characterIndex = characters.index(palindrome[i])
            while characterIndex > 0:
                characterIndex -= 1
                lowestIndexFound = True
            if lowestIndexFound:
                temp = palindrome[i]
                palindrome[i] = characters[characterIndex]
                if palindrome == palindrome[::-1]:
                    palindrome[i] = temp
                    lowestIndexFound = False
                    continue
                break

        # Need to change change last character only
        if not lowestIndexFound:
            characterIndex = characters.index(palindrome[-1])
            palindrome[-1] = characters[characterIndex + 1]
        return "".join(palindrome)