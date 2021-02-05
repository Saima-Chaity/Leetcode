# Partition Labels - https://leetcode.com/problems/partition-labels/
'''A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.
Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 
Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.'''

'''
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(1) to keep data structure last of not more than 26 characters.
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        lastOccurance = {char: index for index, char in enumerate(S)}
        startIndex = 0
        endIndex = 0
        output = []
        for i in range(len(S)):
            endIndex = max(endIndex, lastOccurance[S[i]])
            if i == endIndex:
                output.append(i - startIndex + 1)
                startIndex = i + 1
        return output
            
                    