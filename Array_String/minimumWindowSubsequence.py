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
        minSubsequence = ""
        minLength = float('inf')
        left = 0
        right = 0
        while right < len(S):
            t_index = 0
            while right < len(S): # Find the last character of T in S
                if S[right] == T[t_index]:
                    t_index += 1
                if t_index == len(T):
                    break
                right += 1
            
            if right == len(S):
                break
            
            left = right
            t_index = len(T) - 1
            while left >= 0: # Find the first character of T in S
                if S[left] == T[t_index]:
                    t_index -= 1
                if t_index < 0:
                    break
                left -= 1
            
            if right - left + 1 < minLength: # Update length and substring
                minLength = right - left + 1
                minSubsequence = S[left:right+1]
            
            # Move right pointer to the next position of left pointer, 
            # NOT the next position of right pointer
            right = left + 1
        return minSubsequence
                
        