# Substring with Concatenation of All Words - https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices 
of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
'''
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]

from collections import Counter
class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:

    if not s or not words:
      return []

    wordLength = len(words[0])
    output = []
    for i in range(wordLength):
        word_count = Counter(words) # Reset counter every time
        start, end, count = i, i, len(words)
        while end < len(s):
            current = s[end:end+wordLength]
            if current in word_count:
                word_count[current] -= 1
                if word_count[current] >= 0:
                    count -= 1
            end += wordLength
            
            if count == 0:
                output.append(start)
            
            if end - start == wordLength * len(words): # Ensure consecutive words
                current = s[start:start+wordLength]
                if current in word_count:
                    word_count[current] += 1
                    if word_count[current] > 0:
                        count += 1
                start += wordLength
    return output