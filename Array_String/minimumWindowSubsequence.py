# Minimum Window Subsequence - https://leetcode.com/problems/minimum-window-subsequence/
'''Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple
such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.'''


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def findSubsequence(startIndex):
            j = 0
            while startIndex < len(S):
                if S[startIndex] == T[j]:
                    j += 1
                    if j == len(T):
                        break
                startIndex += 1
            return startIndex if j == len(T) else None

        def findMinWindow(endIndex):
            j = len(T) - 1

            while j >= 0:
                if S[endIndex] == T[j]:
                    j -= 1
                endIndex -= 1
            return endIndex + 1

        minLength = float('inf')
        minWindow = ""
        i = 0

        while i < len(S):
            endOfSubsequence = findSubsequence(i)
            if not endOfSubsequence:
                break
            startOfSubsequence = findMinWindow(endOfSubsequence)

            if endOfSubsequence - startOfSubsequence + 1 < minLength:
                minLength = endOfSubsequence - startOfSubsequence + 1
                minWindow = S[startOfSubsequence:endOfSubsequence + 1]
            i = startOfSubsequence + 1
        return minWindow