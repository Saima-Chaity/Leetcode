'''Number of Good Ways to Split a String
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q
where its concatenation is equal to s and the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s.

Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").
'''

from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:

        s_counts = Counter(s)
        mapping = Counter()
        result = 0
        for i in range(len(s)):
            mapping[s[i]] += 1
            s_counts[s[i]] -= 1

            if s_counts[s[i]] == 0:
                s_counts.pop(s[i])

            if len(mapping) == len(s_counts):
                result += 1
        return result