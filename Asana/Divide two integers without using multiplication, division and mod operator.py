'''Divide two integers without using multiplication, division and mod operator
Input : a = 10, b = 3
Output : 3

Input : a = 43, b = -8
Output :  -5
'''

def divide(dividend, divisor):
    sign = 1
    if dividend < 0 or divisor < 0:
        sign = -1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return sign * quotient


# Driver code
a = 10
b = 3
print(divide(a, b))

a = 43
b = -8
print(divide(a, b))