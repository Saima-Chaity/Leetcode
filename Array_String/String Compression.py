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


class Solution:
    def compress(self, chars: List[str]) -> int:

        def addCharCount(indexPosition, charCount):
            if len(str(charCount)) > 1:
                for count in str(charCount):
                    chars[indexPosition] = str(count)
                    indexPosition += 1
            else:
                chars[indexPosition] = str(charCount)
                indexPosition += 1
            return indexPosition, charCount

        def setChar(indexPosition, prevChar, charCount):
            chars[indexPosition] = char
            indexPosition += 1
            prevChar = char
            charCount = 1
            return indexPosition, prevChar, charCount

        charCount = 0
        prevChar = ""
        indexPosition = 0

        for char in chars:
            if not prevChar:
                indexPosition, prevChar, charCount = setChar(indexPosition, prevChar, charCount)
            elif char == prevChar:
                charCount += 1
            elif char != prevChar:
                if charCount > 1:
                    indexPosition, charCount = addCharCount(indexPosition, charCount)
                indexPosition, prevChar, charCount = setChar(indexPosition, prevChar, charCount)

        if charCount > 1:
            indexPosition, charCount = addCharCount(indexPosition, charCount)

        return len(chars[:indexPosition])
