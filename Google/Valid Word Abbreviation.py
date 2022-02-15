'''Valid Word Abbreviation - https://leetcode.com/problems/valid-word-abbreviation/

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths.
The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
'''


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = 0
        j = 0
        number = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                number = 10 * number + int(abbr[j])
                if number == 0:
                    return False
                j += 1
            else:
                i += number
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                number = 0
                i += 1
                j += 1

        i += number
        return i == len(word) and j == len(abbr)

