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