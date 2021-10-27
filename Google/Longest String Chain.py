'''Longest String Chain - https://leetcode.com/problems/longest-string-chain/

You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without
changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of
word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
'''


class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def dfs(word):
            if word in memo:
                return memo[word]
            maxLength = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i + 1:]
                if new_word in word_set:
                    maxLength = max(maxLength, 1 + dfs(new_word))
            memo[word] = maxLength
            return memo[word]

        word_set = set(words)
        memo = {}
        longestChain = 0
        for word in words:
            longestChain = max(longestChain, dfs(word))
        return longestChain