# Reverse String - https://leetcode.com/problems/reverse-string/
'''Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place
with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
