# Design Search Autocomplete System - https://leetcode.com/problems/design-search-autocomplete-system/

'''Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').
For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.
Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the
same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences.
Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ')
or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that
have prefix the same as the part of sentence already typed.'''

# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:
#
# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
#
# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
#
# Operation: input('a')
# Output: []

class Trie:
    def __init__(self):
        self.node = dict()
        self.words = list()

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.keyword = ""
        self.cache_count = dict()
        self.trie = Trie()

        for index, sentence in enumerate(sentences):
            self.buildTrie(sentence, self.trie)
            self.cache_count[sentence] = times[index]

    def buildTrie(self, sentence, trie):
        for char in sentence:
            if char not in trie.node:
                trie.node[char] = Trie()
            trie = trie.node[char]
            trie.words.append(sentence)
        return True

    def findSentence(self, keyword):
        trie = self.trie
        for char in keyword:
            if char in trie.node:
                trie = trie.node[char]
            else:
                return []
        return trie.words

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.keyword += c
            sentences = self.findSentence(self.keyword)
            result = []
            for sentence in sentences:
                result.append((self.cache_count[sentence], sentence))
            result = list(set(result))
            return [sentence[1] for sentence in sorted(result, key=lambda x: (-x[0], x[1]))[:3]]
        else:
            self.cache_count[self.keyword] = self.cache_count.get(self.keyword, 0) + 1
            self.buildTrie(self.keyword, self.trie)
            self.keyword = ''
        return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)