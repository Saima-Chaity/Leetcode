# Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/
'''Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True'''

from collections import defaultdict
class WordDictionary:

    def __init__(self):
        self.wordDict = defaultdict(list)

    def addWord(self, word: str) -> None:
        self.wordDict[len(word)].append(word)

    def search(self, word: str) -> bool:
        wordList = self.wordDict[len(word)]
        dotCount = -1
        if word.find(".") != -1:
            dotCount = word.count(".")
        for item in wordList:
            if item == word:
                return True
            elif dotCount != -1:
                currentWord = list(word)
                for i in range(len(item)):
                    if currentWord[i] == ".":
                        currentWord[i] = item[i]
                if "".join(currentWord) == item:
                    return True
                else:
                    continue
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)