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


# Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/
'''Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.'''

class Solution:
    def minCut(self, s: str) -> int:

        def isPalindrome(s, startIndex, endIndex):
            temp = s[startIndex:endIndex+1]
            return temp == temp[::-1]
    
        mapping = {}
        def backTrack(start, s):
            if start >= len(s) or isPalindrome(s, start, len(s)-1) :
                return 0
            
            if start in mapping:
                return mapping[start]
                
            result = float('inf')      
            for i in range(start+1, len(s)+1):
                if i != len(s) and isPalindrome(s, start, i-1):
                    result = min(result, 1 + backTrack(i, s))
            result = result if result != float('inf') else 0
            mapping[start] = result
            return mapping[start]

    
        if isPalindrome(s, 0, len(s)-1):
            return 0
        else:
            return backTrack(0, s)
