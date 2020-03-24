# Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

'''Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if
the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.'''

# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

from collections import defaultdict
class Solution:
  def subarraysWithKDistinct(self, A, K):

    def subArray(A, K):
      right = 0
      left = 0
      freq = defaultdict(int)
      counter = 0
      result = 0

      while right < len(A):
        freq[A[right]] += 1
        if freq[A[right]] == 1:
          counter += 1
        right += 1

        while left < right and counter > K:
          freq[A[left]] -= 1
          if freq[A[left]] == 0:
            counter -= 1
          left += 1

        result += right - left
      return result

    output = subArray(A, K) - subArray(A, K-1)
    return output

print(Solution.subarraysWithKDistinct((), [1,2,1,2,3], 2))


# Longest Substring with At Most Two Distinct Characters - https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

'''Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.'''

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

from collections import defaultdict


class Solution:
  def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

    if not s:
      return 0

    right = 0
    left = 0
    freq = defaultdict(int)
    counter = 0
    maxLength = 0

    while right < len(s):
      freq[s[right]] += 1
      if freq[s[right]] == 1:
        counter += 1
      right += 1

      while left < right and counter > 2:
        freq[s[left]] -= 1
        if freq[s[left]] == 0:
          counter -= 1
        left += 1
      maxLength = max(maxLength, right - left)
    return maxLength

print(Solution.lengthOfLongestSubstringTwoDistinct((), "eceba"))

# Longest Substring with At Most K Distinct Characters - https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

'''Given a string, find the length of the longest substring T that contains at most k distinct characters.'''

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.

class Solution:
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

    if not s or not k:
      return 0

    right = 0
    left = 0
    freq = defaultdict(int)
    counter = 0
    maxLength = 0

    while right < len(s):
      freq[s[right]] += 1
      if freq[s[right]] == 1:
        counter += 1
      right += 1

      while left < right and counter > k:
        freq[s[left]] -= 1
        if freq[s[left]] == 0:
          counter -= 1
        left += 1
      maxLength = max(maxLength, right - left)
    return maxLength


# Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''Given a string, find the length of the longest substring without repeating characters.'''

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:

    if not s:
      return 0

    right = 0
    left = 0
    freq = defaultdict(int)
    counter = 0
    maxLength = 0

    while right < len(s):
      freq[s[right]] += 1
      if freq[s[right]] == 1:
        counter += 1
      right += 1

      while left < right and counter < right - left:
        freq[s[left]] -= 1
        if freq[s[left]] == 0:
          counter -= 1
        left += 1
      maxLength = max(maxLength, right - left)
    return maxLength


# Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
'''Given a string S and a string T, find the minimum window in S which will contain all the characters in T in 
complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"'''

from collections import defaultdict, Counter

class Solution:
  def minWindow(self, s: str, t: str) -> str:

    if not s or not t:
      return ""

    left = 0
    minValue = ''
    counter = 0
    target_counter = Counter(t)

    for right in range(len(s)):
      if target_counter[s[right]] > 0:
        counter += 1
      target_counter[s[right]] -= 1

      while counter == len(t):
        if not minValue or right - left + 1 < len(minValue):
          minValue = s[left:right + 1]
        target_counter[s[left]] += 1
        if target_counter[s[left]] > 0:
          counter -= 1
        left += 1
    return minValue


# Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.'''

# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]

from collections import Counter

class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:

    p_counts = Counter(p)
    s_counts = Counter()
    output = []

    if len(s) < len(p):
      return []

    for right in range(len(s)):
      s_counts[s[right]] += 1
      if right >= len(p):
        if s_counts[s[right - len(p)]] == 1:
          del s_counts[s[right - len(p)]]
        else:
          s_counts[s[right - len(p)]] -= 1

      if p_counts == s_counts:
        output.append(right - len(p) + 1)
    return output



# Substring with Concatenation of All Words - https://leetcode.com/problems/substring-with-concatenation-of-all-words/
'''You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices 
of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
'''
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]

from collections import Counter

class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:

    if not s or not words:
      return []

    eachWordLength = len(words[0])
    result = []

    for i in range(eachWordLength):
      words_count = Counter(words)
      left, right, count = i, i, len(words)

      while right < len(s):
        currStr = s[right:right + eachWordLength]
        if currStr in words_count:
          words_count[currStr] -= 1
          if words_count[currStr] >= 0:
            count -= 1
        right += eachWordLength

        if count == 0:
          result.append(left)

        if right - left == len(words) * eachWordLength:
          currStr = s[left:left + eachWordLength]
          if currStr in words_count:
            words_count[currStr] += 1
            if words_count[currStr] > 0:
              count += 1
          left += eachWordLength

    return result
