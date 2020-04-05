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


# Using Trie
class Solution:
    def findAllConcatenatedWordsInADict(self, words):

        self.trie = {}

        def buildTrie(word):
            t = self.trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t["#"] = "#"

        for word in words:
            buildTrie(word)

        result = []
        for word in words:
            if self.helper(word, 0, len(word) - 1, 0):
                result.append(word)
        return result

    def helper(self, word, start, end, count):
        t = self.trie
        for i in range(start, end + 1):
            if word[i] in t:
                t = t[word[i]]
                if "#" in t:
                    if i == end:
                        return count >= 1
                    elif self.helper(word, i + 1, end, count + 1):
                        return True
            else:
                break
        return False


