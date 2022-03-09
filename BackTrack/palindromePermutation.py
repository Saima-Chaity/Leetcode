# Palindrome Permutation - https://leetcode.com/problems/palindrome-permutation/
'''Given a string, determine if a permutation of the string could form a palindrome.
Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true'''

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        oddCount = 0
        mapping = {}
        for char in s:
            mapping[char] = mapping.get(char, 0) + 1
            if mapping[char] % 2 == 0:
                oddCount -= 1
            else:
                oddCount += 1
        return oddCount <= 1

# Palindrome Permutation II - https://leetcode.com/problems/palindrome-permutation-ii/
'''Given a string s, return all the palindromic permutations (without duplicates) of it. 
Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []'''

from collections import Counter
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
        s_count = Counter(s)
        # If the number of characters with odd number of occurences exceeds 1, 
        # it indicates that no palindromic permutation is possible for s
        mid = [char for char, freq in s_count.items() if freq%2==1]
        if len(mid) > 1:
            return []
        mid = "" if mid == [] else mid[0]
        half_s = "".join([char * (freq//2) for char, freq in s_count.items()]) # Take half of the string
        
        output = []
        def backTrack(path, visited):
            if len(path) == len(half_s):
                path = path + mid + path[::-1]
                output.append(path)
                return
            for i in range(0, len(half_s)):
                if not visited[i]:
                    if i > 0 and not visited[i-1] and half_s[i] == half_s[i-1]:
                        continue
                    visited[i] = True
                    backTrack(path+half_s[i], visited)
                    visited[i] = False

        visited = [False] * len(s)
        backTrack("", visited)
        return output

    