'''Alien Dictionary - https://leetcode.com/problems/alien-dictionary/

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted
lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new
language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s
comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same,
then s is smaller if and only if s.length < t.length.

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
'''


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        def dfs(node):
            if node in seen:
                return seen[node]
            seen[node] = False
            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False
            seen[node] = True
            output.append(node)
            return True

        adj_list = {char: [] for word in words for char in word}
        for firstWord, secondWord in zip(words, words[1:]):
            for c, d in zip(firstWord, secondWord):
                if c != d:
                    adj_list[d].append(c)
                    break
            else:
                if len(secondWord) < len(firstWord):
                    return ""

        output = []
        seen = {}
        for node in adj_list:
            if not dfs(node):
                return ""
        return "".join(output)