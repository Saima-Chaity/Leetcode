# Concatenated Words - https://leetcode.com/problems/concatenated-words/

'''Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.'''

# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        wordList = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordList and suffix in wordList:
                    memo[word] = True
                    break
                elif prefix in wordList and dfs(suffix):
                    memo[word] = True
                    break
                elif suffix in wordList and dfs(prefix):
                    memo[word] = True
                    break
            return memo[word]

        output = []
        for word in words:
            if dfs(word):
                output.append(word)
        return output


