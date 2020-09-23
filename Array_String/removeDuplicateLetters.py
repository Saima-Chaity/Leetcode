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
		visited = set()
		last_occurance = {char:index for index, char in enumerate(s)}
		
		for index, char in enumerate(s):
				if char not in visited:
						while stack and char < stack[-1] and index < last_occurance[stack[-1]]: # Check if the character is greater than the current characters																																		
								visited.discard(stack.pop())																				# if the character can be removed because it occurs later on
						stack.append(char)
						visited.add(char)
		return "".join(stack)
							