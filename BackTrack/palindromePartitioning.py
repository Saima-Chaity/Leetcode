# Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/
'''Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output=[]
        def backTrack(start, end, path, s):
            if start == end:
                output.append(path[:])
            
            for i in range(start, end):
                current = s[start:i+1]
                if current == current[::-1]:
                    backTrack(i+1, end, path+[current], s)
                
        backTrack(0, len(s), [], s)
        return output