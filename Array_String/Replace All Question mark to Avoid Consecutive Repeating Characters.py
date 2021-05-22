'''Replace All ?'s to Avoid Consecutive Repeating Characters

Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters
into lower case letters such that the final string does not contain any consecutive repeating characters.
You cannot modify the non '?' characters.

It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.

Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution,
return any of them. It can be shown that an answer is always possible with the given constraints.

Example 1:

Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid
modification as the string will consist of consecutive repeating characters in "zzs".'''


class Solution:
    def modifyString(self, s: str) -> str:

        chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "u", "s", "t",
                 "v", "w", "x", "y", "z"]

        s = list(s)
        if len(s) == 1 and s[0] == "?":
            return "a"

        if s[-1] == "?":
            for index, char in enumerate(chars):
                if char != s[-2]:
                    s[-1] = char
                    break

        if s[0] == "?":
            for index, char in enumerate(chars):
                if char != s[1]:
                    s[0] = char
                    break

        for i in range(len(s)):
            if s[i] == "?":
                for index, char in enumerate(chars):
                    if char != s[i - 1] and char != s[i + 1]:
                        s[i] = char
                        break
        return "".join(s)





