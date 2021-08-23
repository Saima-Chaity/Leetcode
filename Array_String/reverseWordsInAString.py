# Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/
'''Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated
by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
'''

class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split(" ")
        s = s[::-1]
        output = ""
        for word in s:
            if word != "":
                output = output + " " + word
        return output.strip()


# o(1) space
class Solution:
    def reverseWords(self, s: str) -> str:

        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        s = s.strip()
        s = list(s)
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                end = s.index(' ', start)
                reverse(s, start, end - 1)
                start = end + 1
        reverse(s, start, len(s) - 1)
        reverse(s, 0, len(s) - 1)

        j = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i] == " ":
                continue
            else:
                s[j] = s[i]
                j += 1
        return "".join(s[:j])

# Reverse Words in a String II - https://leetcode.com/problems/reverse-words-in-a-string-ii/
'''Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.

Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]
'''

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverseWord(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        reverseWord(0, len(s) - 1)
        left = 0
        for i in range(len(s)):
            if s[i] == " ":
                reverseWord(left, i - 1)
                left = i + 1
        reverseWord(left, len(s) - 1)



# Reverse Words in a String III - https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''Given a string, you need to reverse the order of characters in each word within a 
sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any 
extra space in the string.'''

class Solution:
    def reverseWords(self, s: str) -> str:

        if not s:
            return ""

        splitedString = s.split(' ')

        for i in range(len(splitedString)):
            splitedString[i] = splitedString[i][::-1]
        return " ".join(splitedString)