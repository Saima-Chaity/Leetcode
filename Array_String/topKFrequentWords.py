# Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/
'''Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the
same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.'''

# Using heap
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapping = Counter(words)
        heap = []
        output = []
        for word, freq in mapping.items():
            heapq.heappush(heap, (-freq, word))

        for i in range(k):
            freq, word = heapq.heappop(heap)
            output.append(word)
        return output

