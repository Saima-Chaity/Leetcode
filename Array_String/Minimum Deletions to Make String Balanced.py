'''Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of
indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
'''

class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        b_count = 0
        char_a = "a"
        for i in range(len(s)):
            if char_a == s[i]:
                count = min(b_count, count + 1)
            else:
                b_count += 1
        return count


'''The idea is to use two pointers i and j where i traverses from left to right and j traverses from right to left.
While traversing right, get to the first position where s[i] == 'b' and similarly while traversing left, get to the 
first position where s[j] == 'a'. We also keep on adjusting the count of 'a' and 'b' accordingly. Now we reach to a 
point where s[0:i] is all 'a' and s[j+1:] is all 'b'. At this point we need to decide whether we want to delete 'a' 
or 'b'. So we go greedy and delete that char whose count is less. So if count_a < count_b, we delete char 'a' else 
we delete char 'b'.'''

# Another approach
class Solution:
    def minimumDeletions(self, s: str) -> int:

        a_count = 0
        for char in s:
            a_count += 1 if char == 'a' else 0

        b_count = len(s) - a_count
        i = 0
        j = len(s) - 1
        result = 0

        while i < j:
            while i < j and s[i] == 'a':
                i += 1
                a_count -= 1

            while i < j and s[j] == 'b':
                j -= 1
                b_count -= 1

            if a_count and b_count:
                if a_count < b_count:
                    j -= 1
                    a_count -= 1
                    result += 1
                else:
                    i += 1
                    b_count -= 1
                    result += 1
        return result