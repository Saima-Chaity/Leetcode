# Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to
any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        if len(digits) == 1:
            return list(mapping[int(digits)])

        def generateCombination(combination, nextDigits):
            if len(nextDigits) == 0:
                output.append(combination)
            else:
                for letter in mapping[int(nextDigits[0])]:
                    generateCombination(combination + letter, nextDigits[1:])

        output = []

        if digits:
            generateCombination("", digits)
        return output



