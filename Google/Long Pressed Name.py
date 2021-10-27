'''Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

Your friend is typing his name into a keyboard. Sometimes, when typing a character c,
the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that
it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
'''

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        if len(typed) < len(name):
            return False
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False
            name_count = 0
            typed_count = 0
            while i + 1 < len(name) and name[i + 1] == name[i]:
                name_count += 1
                i += 1
            while j + 1 < len(typed) and typed[j + 1] == typed[j]:
                typed_count += 1
                j += 1

            if name_count > typed_count:
                return False
            i += 1
            j += 1

        if i < len(name) or j < len(typed):
            return False

        return True



