'''Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
'''

from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        groupings = defaultdict(list)
        for word in words:
            groupings[word[0]].append(word[1:])

        result = 0
        for char in s:
            current_words = groupings[char]
            groupings[char] = []
            for word in current_words:
                if not word:
                    result += 1
                else:
                    groupings[word[0]].append(word[1:])
        return result