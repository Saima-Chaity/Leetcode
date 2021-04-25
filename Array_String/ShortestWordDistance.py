# Shortest Word Distance - https://leetcode.com/problems/shortest-word-distance/
'''Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.'''

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        l1 = -1
        l2 = -1
        shortestDistance = float('inf')
        for index, word in enumerate(words):
            if word == word1:
                l1 = index
            elif word == word2:
                l2 = index
            if l1 != -1 and l2 != -1:
                shortestDistance = min(shortestDistance, abs(l1 - l2))
        return shortestDistance


# Shortest Word Distance II - https://leetcode.com/problems/shortest-word-distance-ii/
'''Design a class which receives a list of words in the constructor, and implements a method that takes two 
words word1 and word2 and return the shortest distance between these two words in the list. Your method will 
be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.'''

from collections import defaultdict
class WordDistance:

    def __init__(self, words: List[str]):
        self.wordsList = words
        self.mapping = defaultdict(list)
        for index, word in enumerate(words):
            self.mapping[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        shortestDistance = float('inf')
        location1 = self.mapping[word1]
        location2 = self.mapping[word2]
        l1 = 0
        l2 = 0
        while l1 < len(location1) and l2 < len(location2):
            shortestDistance = min(shortestDistance, abs(location1[l1] - location2[l2]))
            if location1[l1] < location2[l2]:
                l1 += 1
            else:
                l2 += 1
        return shortestDistance

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)


# Shortest Word Distance III - https://leetcode.com/problems/shortest-word-distance-iii/
'''Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.'''

from collections import defaultdict
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        self.mapping = defaultdict(list)
        for index, word in enumerate(wordsDict):
            self.mapping[word].append(index)

        shortestDistance = float('inf')
        location1 = self.mapping[word1]
        location2 = self.mapping[word2]
        l1 = 0
        l2 = 0
        while l1 < len(location1) and l2 < len(location2):
            if l1 != l2 and word1 == word2 or word1 != word2:
                shortestDistance = min(shortestDistance, abs(location1[l1] - location2[l2]))
            if location1[l1] < location2[l2]:
                l1 += 1
            else:
                l2 += 1
        return shortestDistance
    
            