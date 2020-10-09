# Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/
'''Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
'''

class Solution:
	def removeDuplicateLetters(self, s) -> int:
		stack = []
        last_occurance = {char:index for index, char in enumerate(s)}
        for index, char in enumerate(s):
            if char not in stack:
                while stack and stack[-1] > char and last_occurance[stack[-1]] > index: # Check if the character is greater than the current characters	
                    stack.pop()															# if the character can be removed because it occurs later on
                stack.append(char)
        return "".join(stack)


# Similar question
# Smallest Subsequence of Distinct Characters - https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
'''Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.
Example 1:
Input: "cdadabcc"
Output: "adbc"
'''

class Solution:
	def smallestSubsequence(self, text: str) -> str:
		stack = []
        last_occurance = {char:index for index, char in enumerate(s)}
        for index, char in enumerate(s):
            if char not in stack:
                while stack and stack[-1] > char and last_occurance[stack[-1]] > index:
                    stack.pop()
                stack.append(char)
        return "".join(stack)