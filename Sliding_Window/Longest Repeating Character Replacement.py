'''Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above
operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.'''

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Max_length the longest subsequence without repeating chars and k changes
        # Max_count is the high count chars in the answer subsequence
        maxLength = maxCount = 0
        count = defaultdict(int)
        for i in range(len(s)):
            # Count keeps track of the chars in the we are looking at subsequence
            count[s[i]] += 1
            # key idea(2): Find the new max_count. This is much like Kadane's
            # Where we only consider if the new length exceedes the max_length overall
            maxCount = max(maxCount, count[s[i]])
            # Key idea (1): the answer is always max_count + k.
            if maxLength < k + maxCount:
                maxLength += 1
            else:
            # key idea(3) This removes the char at the start of the subsequence s[i-max_length]
            # This serves as "correction" for the subsequence problem
                count[s[i-maxLength]] -= 1
        return maxLength