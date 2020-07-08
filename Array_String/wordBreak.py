# Word Break - https://leetcode.com/problems/word-break/
'''Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".'''

# DFS and Memoization
class Solution:
    def wordBreak(self, s: str, wordDict:List[str]) -> bool:
        if not wordDict:
            return False
        def dfs(s):
            if s == "":
                return True
            for i in range(len(s)):
                current = s[:i+1]
                if s[i+1:] in mapping and mapping[s[i+1:]] is False:
                    continue
                if current in wordDict:
                    result = dfs(s[i+1:])
                    if result:
                        return True
                    mapping[s[i+1:]] = result
            return False
        mapping = {}
        return dfs(s)

# BFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()
        q = deque([0])
        while q:
            start = q.popleft()
            if start not in visited:
                for end in range(start + 1, len(s) + 1):
                    word = s[start:end]
                    if word in wordDict:
                        q.append(end)
                        if end == len(s):
                            return True
                visited.add(start)
        return False


# Word Break II - https://leetcode.com/problems/word-break-ii/
'''Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such 
possible sentences.

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.word_break(s, wordDict, {})

    def word_break(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []

        output = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(s) == len(word) and s == word:
                output.append(word)
            else:
                restOfTheWord = self.word_break(s[len(word):], wordDict, memo)
                for item in restOfTheWord:
                    sentence = word + " " + item
                    output.append(sentence)
        memo[s] = output
        return output

# Second approach
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.dict = wordDict
        self.cache = {}
        return self.word_break(s)

    def word_break(self, s):
        if s in self.cache:
            return self.cache[s]
        if not s:
            return []
        output = []
        for i in range(len(s)):
            if s[:i + 1] in self.dict:
                if i == len(s) - 1:
                    output.append(s[:i + 1])
                else:
                    restOfTheResult = self.word_break(s[i + 1:])
                    for item in restOfTheResult:
                        new_word = s[:i + 1] + ' ' + item
                        output.append(new_word)
        self.cache[s] = output
        return output
