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