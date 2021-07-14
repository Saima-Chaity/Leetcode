# Group Anagrams - https://leetcode.com/problems/group-anagrams/
'''Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]'''

# Time complexity - O(NKlogK)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for word in strs:
            mapping[tuple(sorted(word))].append(word)
        return mapping.values()


# Time complexity - 0(NK) - N is the length of strs, and K is the maximum length of a string in strs
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) <= 1:
            return [strs]

        output = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for i in range(len(word)):
                count[ord(word[i]) - ord('a')] += 1
            output[tuple(count)].append(word)
        return output.values()