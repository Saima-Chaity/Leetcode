# Fraction to Recurring Decimal - https://leetcode.com/problems/fraction-to-recurring-decimal/
'''Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Input: numerator = 1, denominator = 2
Output: "0.5"

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        output = []
        if numerator * denominator < 0:
            output.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        result = (numerator // denominator)
        remainder = numerator % denominator
        output.append(str(result))
        if not remainder:
            return "".join(output)
        output.append(".")
        mapping = {}
        while remainder:
            if remainder in mapping:
                output.insert(mapping[remainder], "(")
                output.append(")")
                break

            mapping[remainder] = len(output)
            n, remainder = divmod(remainder * 10, denominator)
            output.append(str(n))
        return "".join(output)
