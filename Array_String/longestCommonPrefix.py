# Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/
'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: ["flower","flow","flight"]
Output: "fl"'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if len(prefix) == 0:
                    return ""
        return prefix

