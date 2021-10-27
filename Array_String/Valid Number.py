# Valid Number - https://leetcode.com/problems/valid-number/
'''Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. It would be best if you
gathered all requirements up front before implementing one. However, here is a list of
characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.'''


class Solution:
    def isNumber(self, s: str) -> bool:

        '''Four checks:
            1. If char == + or char == -, then prev char (if there is) must be "e"
            2. "." cannot appear twice or after e
            3. "e" cannot appear twice, and there must be at least one digit before and after e
            4. All other non-digit char is invalid'''

        if len(s) == 1 and s[0] == '.' or s[0] == 'e':
            return False

        if len(s) > 0 and s[-1] in "+-e":
            return False

        dotFound = False
        eFound = False
        digitFound = False

        for i in range(len(s)):
            char = s[i]
            if char in "+-":
                if i > 0 and s[i - 1] not in "Ee":
                    return False
            elif char == ".":
                if eFound or dotFound:
                    return False
                dotFound = True
            elif char in "Ee":
                if eFound or not digitFound:
                    return False
                eFound = True
                digitFound = False
            elif char.isdigit():
                digitFound = True
            else:
                return False
        return digitFound