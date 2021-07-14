'''Maximum Length of a Concatenated String with Unique Characters
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which
have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.'''

'''Time Complexity: O(2^N) 
Auxiliary Space: O(N * 2^N)
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        result = float('-inf')

        def backTrack(path, index):
            nonlocal result
            if len(path) == len(set(path)):
                result = max(result, len(path))
            else:
                return
            for i in range(index, len(arr)):
                backTrack(path + arr[i], i + 1)

        backTrack("", 0)
        return result