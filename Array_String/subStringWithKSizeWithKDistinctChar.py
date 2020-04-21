# Substrings of size K with K distinct chars

'''Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.'''

# Input: s = "abcabc", k = 3
# Output: ["abc", "bca", "cab"]
#
# Input: s = "abacab", k = 3
# Output: ["bac", "cab"]

from collections import defaultdict
class Solution:
    def subString(s, k):
        if not s or not k:
            return 0

        right = 0
        freq = defaultdict()
        result = []

        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = right
                right += 1
                if len(freq) == k:
                    lowestIndex = min(freq.values())
                    substr = s[lowestIndex:right]
                    if substr not in result:
                        result.append(substr)
                    del freq[s[lowestIndex]]
            else:
                lowestIndex = min(freq.values())
                del freq[s[lowestIndex]]
        return result

print(Solution.subString("awaglknagawunagwkwagl", 4))

# output : ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]






