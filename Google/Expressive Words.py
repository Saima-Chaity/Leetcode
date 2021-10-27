'''Expressive Words - https://leetcode.com/problems/expressive-words/

Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal
to s by any number of applications of the following extension operation: choose a group consisting of characters c,
and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get
"helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll"
to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension
operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.

Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
'''


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def getCount(s, word):
            i = 0
            j = 0
            while i < len(s) or j < len(word):
                if i < len(s):
                    s_count = 0
                    s_char = s[i]
                    while i < len(s) and s[i] == s_char:
                        s_count += 1
                        i += 1
                if j < len(word):
                    word_count = 0
                    word_char = word[j]
                    while j < len(word) and word[j] == word_char:
                        word_count += 1
                        j += 1
                if s_char == word_char and ((s_count >= 3 and word_count <= s_count) or word_count == s_count):
                    continue
                else:
                    return False
            return True

        validCount = 0
        for word in words:
            if getCount(s, word):
                validCount += 1
        return validCount

