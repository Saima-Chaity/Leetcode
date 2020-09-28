# Group Anagrams - https://leetcode.com/problems/group-anagrams/
'''Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for word in strs:
            mapping[tuple(sorted(word))].append(word)
        return mapping.values()


# Group Shifted Strings - https://leetcode.com/problems/group-shifted-strings/
'''Given a string, we can "shift" each of its letter to its successive letter, 
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, 
group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]'''

class Solution:
  def groupStrings(self, strings: List[str]) -> List[List[str]]:
    output = collections.defaultdict(list)
    for word in strings:
      key = ()
      for i in range(1, len(word)):
        difference = (ord(word[i]) - ord(word[i-1])) % 26
        key += (difference, )
      output[key].append(word)
    return output.values()
    
