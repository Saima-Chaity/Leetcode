# Construct K Palindrome Strings - https://leetcode.com/problems/construct-k-palindrome-strings/
'''Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.
 
Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.'''

from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        # Condition 1. odd characters <= k
        # Count the occurrences of all characters.
        # If one character has odd times occurrences,
        # there must be at least one palindrome,
        # with odd length and this character in the middle.
        # So we count the characters that appear odd times,
        # the number of odd character should not be bigger than k.

        # Condition 2. k <= s.length()
        # Also, if we have one character in each palindrome,
        # we will have at most s.length() palindromes,
        # so we need k <= s.length().

        # The above two condition are necessary and sufficient conditions for this problem.
        # So we return odd <= k <= n
        
        s_count = Counter(s)
        odd_count = 0
        for char, freq in s_count.items():
            odd_count += freq % 2
        return odd_count <= k and k <= len(s)
        
        