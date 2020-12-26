# Group Shifted Strings - https://leetcode.com/problems/group-shifted-strings/
'''Given a string, we can "shift" each of its letter to its successive letter, for example: 
"abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings 
that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]'''

from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def getAsciiValue(string):
            totalValue = []
            for i in range(len(string) - 1):
                totalValue.append(str((ord(string[i + 1]) - ord(string[i])) % 26))
            return "".join(totalValue)

        mapping = defaultdict(list)
        for item in strings:
            asciiValue = getAsciiValue(item)
            mapping[asciiValue].append(item)
        return mapping.values()