'''Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

Given an array of strings words representing an English Dictionary, return the longest word in words that can
be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
'''

class Solution:
    def longestWord(self, words: List[str]) -> str:
        def check_words(word):
            new_word = ""
            for char in word:
                if not new_word and char not in word_dict:
                    return ""
                else:
                    new_word += char
                    if new_word not in word_dict:
                        return ""
            output.append(new_word)

        word_dict = set(words)
        output = []
        for i in range(len(words) - 1, -1, -1):
            if output and len(output[-1]) > len(words[i]):
                continue
            check_words(words[i])

        if not output:
            return ""

        output.sort(key=lambda x: (-len(x), x))
        return output[0]
