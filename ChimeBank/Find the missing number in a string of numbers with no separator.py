'''Find the missing number in a string of numbers with no separator

Given a string consisting of some numbers, not separated by any separator. The numbers are positive integers
and the sequence increases by one at each number except the missing number. The task is to find the missing number.
The numbers will have no more than six digits. Print -1 if the input sequence is not valid.

Examples:

Input  : 89101113
Output : 12

Input  : 9899101102
Output : 100

Input  : 596597598600601602:
Output : 599

Input  : 909192939495969798100101
Output : 99

Input  : 11111211311411511
Output : -1
'''

class Solution:
    def parse(digits):

        def splitStr(digits, n):
            return digits[:n], digits[n:]

        for n in range(1, 7):
            expected, remainder = splitStr(digits, n)
            missingNumber = []
            while len(missingNumber) <= 1 and remainder:
                expected = str(int(expected)+1)
                actual, remainder = splitStr(remainder, len(expected))
                if actual != expected:
                    missingNumber.append(expected)
                    remainder = actual + remainder
            if len(missingNumber) == 1:
                return int(missingNumber[0])
        return -1

print(Solution.parse("89101113")) # 12
print(Solution.parse("9899101102")) # 100
print(Solution.parse("596597598600601602")) # 599
print(Solution.parse("909192939495969798100101")) # 99
print(Solution.parse("11111211311411511")) # -1
print(Solution.parse("910111213")) # -1
print(Solution.parse("99100101102103")) # -1
print(Solution.parse("999100010011002")) # -1
print(Solution.parse("9899100101103104105")) # 102
print(Solution.parse("176517661768")) # 1767
print(Solution.parse("8632456863245786324598632460")) # 8632458