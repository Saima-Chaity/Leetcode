# Verifying an Alien Dictionary - https://leetcode.com/problems/verifying-an-alien-dictionary/
'''In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.'''


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_index = {char: index for index, char in enumerate(order)}
        for i in range(len(words) - 1):
            firstWord = words[i]
            secondWord = words[i + 1]
            for i in range(min(len(firstWord), len(secondWord))):
                if firstWord[i] == secondWord[i]:
                    continue
                else:
                    if order_index[firstWord[i]] > order_index[secondWord[i]]:
                        return False
                break
            else:
                if len(firstWord) > len(secondWord):
                    return False
        return True


