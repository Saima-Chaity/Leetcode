# Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/
'''Given a string, sort it in decreasing order based on the frequency of characters.

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.'''


# Time - 0(nlogm)
from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:

        mapping = Counter(s)
        heap = []
        output = ""
        for char, freq in mapping.items():
            heapq.heappush(heap, (-freq, char))

        while len(heap) > 0:
            freq, char = heapq.heappop(heap)
            output += char * abs(freq)
        return output


# Bucket sort time - 0(n)
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        if not s:
            return s

        s_count = Counter(s)
        maxValues = max(s_count.values())
        bucket = [[] for _ in range(maxValues + 1)]
        for char, freq in s_count.items():
            bucket[freq].append(char)

        output = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for char in bucket[i]:
                    output.append(char * i)
        return "".join(output)
