'''String Compression - https://leetcode.com/problems/string-compression/

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

Follow up:
Could you solve it using only O(1) extra space?

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
'''

# O(n) time and O(1) space
class Solution:
    def compress(self, chars: List[str]) -> int:

        left, i = 0, 0
        while i < len(chars):
            length, char = 1, chars[i]
            while i + 1 < len(chars) and char == chars[i + 1]:
                i += 1
                length += 1
            chars[left] = char
            if length > 1:
                length = str(length)
                chars[left + 1:left + 1 + len(length)] = length
                left += len(length)
            left += 1
            i = i + 1
        return left
