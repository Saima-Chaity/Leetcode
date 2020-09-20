# Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
'''You are given a string s that consists of lower case English letters and brackets. 
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.'''

import heapq
class Solution:
    def reverseParentheses(self, s: str) -> str:
        left = []
        right = {}
        for index, char in enumerate(s):
            if char == "(":
                heapq.heappush(left, (-index))
            elif char == ")":
                right[index] = char

        while len(left) > 0 and len(right) > 0:
            leftIndex = heapq.heappop(left)
            rightIndex = 0
            for index, bracket in right.items():
                if index > abs(leftIndex):
                    rightIndex = index
                    del right[index]
                    break

            reversedStr = s[abs(leftIndex)+1:rightIndex][::-1]
            s = s[:abs(leftIndex)+1] + reversedStr + s[rightIndex:]
        
        output = ""
        for char in s:
            if char == "(":
                char = ""
            elif char == ")":
                char = ""
            else:
                output += char
        return output
       

# Using stack
class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = [""]
        for char in s:
            if char == "(":
                stack.append("")
            elif char == ")":
                current = stack.pop()
                stack[-1] += current[::-1]
            else:
                stack[-1] += char
        return "".join(stack)
