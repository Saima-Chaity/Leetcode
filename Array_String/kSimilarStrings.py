# K-Similar Strings - https://leetcode.com/problems/k-similar-strings/
'''Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters
in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1'''

from collections import deque

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        def neighbor(currentStr):
            for i, char in enumerate(currentStr):
                if char != B[i]:
                    break
            listOfA = list(currentStr)
            for j in range(i + 1, len(currentStr)):
                if currentStr[j] == B[i]:
                    listOfA[i], listOfA[j] = listOfA[j], listOfA[i]
                    yield "".join(listOfA)
                    listOfA[j], listOfA[i] = listOfA[i], listOfA[j]

        q = deque([A])
        seen = {A: 0}

        while q:
            currentStr = q.popleft()
            if currentStr == B:
                return seen[currentStr]
            for newStr in neighbor(currentStr):
                if newStr not in seen:
                    seen[newStr] = seen[currentStr] + 1
                    q.append(newStr)
        return 0