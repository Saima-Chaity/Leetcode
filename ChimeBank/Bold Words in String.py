'''Bold Words in String - https://leetcode.com/problems/bold-words-in-string/

Given a set of keywords words and a string S, make all appearances of all keywords in S bold.
Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the
tags should form a valid combination.

For example, given that words = [“ab”, “bc”] and S = “aabcd”, we should return “a<b>abc</b>d”.
Note that returning “a<b>a<b>b</b>c</b>d” would use more tags, so it is incorrect.

Note:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        self.trie = TrieNode()
        for word in words:
            self.buildTrie(word)

        self.intervals = []

        for i in range(len(s)):
            node = self.trie
            end = None
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.isWord:
                    end = j + 1
            if end:
                self.mergeIntervals([i, end])

        result = []
        prevEnd = 0
        for start, end in self.intervals:
            result.append(s[prevEnd:start])
            result.append('<b>')
            result.append(s[start:end])
            result.append('</b>')
            prevEnd = end

        result.append(s[prevEnd:])
        return "".join(result)

    def mergeIntervals(self, interval):
        if not self.intervals or self.intervals[-1][1] < interval[0]:
            self.intervals.append(interval)
        else:
            self.intervals[-1][1] = max(self.intervals[-1][1], interval[1])

    def buildTrie(self, word):
        node = self.trie
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True


# O(S ^ 2 * D) runtime, O(S + D) space
from collections import defaultdict
class Solution:
    def boldWords(self, words: List[str], s: str) -> str:

        charDict = defaultdict(set)
        for word in words:
            charDict[word[0]].add((word, len(word)))

        result = []
        currentStart = None
        currentEnd = -1
        for i, char in enumerate(s):
            if char in charDict:
                for word, length in charDict[char]:
                    if s[i:i + length] == word:
                        if currentStart is None:
                            currentStart = i
                        currentEnd = max(currentEnd, i + length - 1)

            if i > currentEnd:
                if currentStart is not None:
                    result.append("<b>" + s[currentStart:currentEnd + 1] + "</b>")
                result.append(char)
                currentStart = None
                currentEnd = i

        if currentStart is not None:
            result.append("<b>" + s[currentStart:currentEnd + 1] + "</b>")

        return "".join(result)
