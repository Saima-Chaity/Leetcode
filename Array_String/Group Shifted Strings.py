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
    '''The key can be represented as a tuple of the "differences" between adjacent characters.
    Characters map to integers (e.g. ord('a') = 97). For example, 'abc' maps to (1,1)
    because ord('b') - ord('a') = 1 and ord('c') - ord('b') = 1
    We need to watch out for the "wraparound" case - for example, 'az' and 'ba' should map to
    the same "shift group" as a + 1 = b and z + 1 = a. Given the above point, the respective
    tuples would be (25,) (122 - 97) and (-1,) (79 - 80) and az and ba would map to different
    groups. This is incorrect.
    To account for this case, we add 26 to the difference between letters (smallest difference possible is -25, za)
    and mod by 26. So, (26 + 122 - 97) % 26 and (26 + 79 - 80) % 26 both equal (25,)'''
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