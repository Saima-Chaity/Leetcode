# Implement strStr() - https://leetcode.com/problems/implement-strstr/
'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0

        h_index = 0
        n_index = 0

        while h_index < len(haystack):
            if haystack[h_index] == needle[n_index]:
                h_index += 1
                n_index += 1
            elif haystack[h_index] != needle[n_index] and n_index > 0:
                h_index = h_index - n_index + 1
                n_index = 0
            else:
                h_index += 1

            if n_index == len(needle):
                return h_index - n_index
        return -1