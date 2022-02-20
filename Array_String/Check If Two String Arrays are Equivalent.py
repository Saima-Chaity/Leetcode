'''Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
'''


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        word1_str = "".join(word1)
        word2_str = "".join(word2)
        if len(word1_str) != len(word2_str):
            return False

        i = 0
        j = 0
        while i < len(word1_str) and j < len(word2_str):
            if word1_str[i] == word2_str[j]:
                i += 1
                j += 1
            else:
                return False
        return True