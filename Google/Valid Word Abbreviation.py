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

        wordIndex = 0
        abbreviation_index = 0
        while abbreviation_index < len(abbr) and wordIndex < len(word):
            char = abbr[abbreviation_index]
            if abbr[abbreviation_index].isdigit():
                if abbr[abbreviation_index] == '0':
                    return False
                abbreviation_number = 0
                while abbreviation_index < len(abbr) and abbr[abbreviation_index].isdigit():
                    abbreviation_number = abbreviation_number * 10 + int(abbr[abbreviation_index])
                    abbreviation_index += 1
                wordIndex += abbreviation_number
                if wordIndex > len(word):
                    return False
            else:
                if char != word[wordIndex]:
                    return False
                elif char == word[wordIndex]:
                    wordIndex += 1
                    abbreviation_index += 1
        return wordIndex == len(word) and abbreviation_index == len(abbr)
