# Verifying an Alien Dictionary - https://leetcode.com/problems/verifying-an-alien-dictionary/
'''In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.'''


class Solution(object):
    def isAlienSorted(self, words, order):

        orderIndex = {char: index for index, char in enumerate(order)}
        for i in range(len(words) - 1):
            for k in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][k] != words[i + 1][k]:
                    if orderIndex[words[i][k]] > orderIndex[words[i + 1][k]]:
                        return False
                    break
            else:
                if len(words[i]) > len(words[i + 1]):
                    return False
        return True

