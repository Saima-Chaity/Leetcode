'''Minimum Deletions to Make Character Frequencies Unique -
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example,
in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
'''

from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:

        s_count = Counter(s)
        seen = set()
        removedCount = 0

        for char, freq in s_count.items():
            while freq in seen:
                freq -= 1
                removedCount += 1
            if freq:
                seen.add(freq)
        return removedCount