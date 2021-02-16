# Word Ladder - https://leetcode.com/problems/word-ladder/
'''Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord: True}

        while q:
            currentWord, length = q.popleft()
            for i in range(len(currentWord)):
                intermediate_combo = currentWord[:i] + "*" + currentWord[i + 1:]
                for word in all_combo_dict[intermediate_combo]:
                    if word == endWord:
                        return length + 1
                    if word not in visited:
                        visited[word] = True
                        q.append((word, length + 1))
                all_combo_dict[intermediate_combo] = {}
        return 0


# Word Ladder II - https://leetcode.com/problems/word-ladder-ii/
'''Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) 
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]'''

from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        output = []
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        q = deque([(beginWord, [beginWord])])
        visited = set([beginWord])
        found = False

        while q and not found:
            localVisited = set() # localVisited is used so that we can visit same word multiple time and get
                                # different combinations
            for _ in range(len(q)):
                currentWord, path = q.popleft()
                for i in range(len(currentWord)):
                    intermediate_combo = currentWord[:i] + "*" + currentWord[i + 1:]
                    for word in all_combo_dict[intermediate_combo]:
                        if word == endWord:
                            found = True # found shortest path
                            output.append(path + [endWord])
                        if word not in visited:
                            localVisited.add(word)
                            q.append((word, path + [word]))
            visited = visited.union(localVisited)
        return output