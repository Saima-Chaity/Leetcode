'''Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix
prefix and the suffix suffix. If there is more than one valid index, return the largest of them.
If there is no such word in the dictionary, return -1.


Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".'''


class Trie:
    def __init__(self):
        self.nodes = dict()
        self.indexes = []

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_trie = Trie()
        self.suffix_trie = Trie()
        self.visited = {}
        for index, word in enumerate(words):
            self.buildTrie(self.prefix_trie, word, index)
            self.buildTrie(self.suffix_trie, word[::-1], index)

    def buildTrie(self, trie, word, index):
        t = trie
        for char in word:
            if char not in t.nodes:
                t.nodes[char] = Trie()
            t.nodes[char].indexes.append(index)
            t = t.nodes[char]
        t.indexes.append(index)

    def find(self, word, trie):
        t = trie
        for char in word:
            if char not in t.nodes:
                return []
            t = t.nodes[char]
        return t.indexes

    def f(self, prefix: str, suffix: str) -> int:
        prefix_indexes = self.find(prefix, self.prefix_trie)
        suffix_indexes = self.find(suffix[::-1], self.suffix_trie)

        self.visited[prefix] = prefix_indexes
        self.visited[suffix] = suffix_indexes

        i = len(prefix_indexes) - 1
        j = len(suffix_indexes) - 1
        while i >= 0 and j >= 0:
            if prefix_indexes[i] == suffix_indexes[j]:
                return prefix_indexes[i]
            if prefix_indexes[i] > suffix_indexes[j]:
                i -= 1
            elif prefix_indexes[i] < suffix_indexes[j]:
                j -= 1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


# One trie
class Trie:
    def __init__(self):
        self.nodes = dict()
        self.indexes = 0

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for index, word in enumerate(words):
            word_length = len(word)
            for j in range(word_length + 1):
                self.buildTrie(word[j:word_length] + "#" + word, index)

    def buildTrie(self, word, index):
        t = self.trie
        for char in word:
            if char not in t.nodes:
                t.nodes[char] = Trie()
            t.nodes[char].indexes = index
            t = t.nodes[char]
        t.indexes = index

    def find(self, word):
        t = self.trie
        for char in word:
            if char not in t.nodes:
                return []
            t = t.nodes[char]
        return t.indexes

    def f(self, prefix: str, suffix: str) -> int:
        result = self.find(suffix + "#" + prefix)
        if result == 0:
            return 0
        if not result:
            return -1
        return result

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


