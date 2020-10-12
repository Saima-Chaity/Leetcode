# Substrings with exactly K distinct chars
'''Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k 
distinct characters. If the given string doesn't have k distinct characters, return 0.'''

# Input: s = "pqpqs", k = 2
# Output: 7
# Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]

class Solution:
  def subString(A, K):
    def findSubString(A, K):
      freq = {}
      left = 0
      right = 0
      count = 0
      while right < len(A):
        if A[right] not in freq:
          freq[A[right]] = 0
        freq[A[right]] += 1

        while len(freq) > K:
          freq[A[left]] -= 1
          if freq[A[left]] == 0:
            del freq[A[left]]
          left += 1
        count += right - left + 1
        right += 1
      return count

    output = findSubString(A, K) - findSubString(A, K - 1)
    return output

print(Solution.subString("pqpqs", 2))  # ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
