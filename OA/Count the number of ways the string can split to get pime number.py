'''count the number of ways the string can split to get pime number

Given a string of length n consisting of digits [0-9], count the number of ways the given string
can be split into prime numbers, each of which is in the range 2 to 100 inclusive. Since the answer
can be large, return the answer modulo 109 + 7. Note: A partition that contains numbers with leading
zeroes will be invalid and the initial string does not contain leading zeroes. Take for example the
input string to be s = "11373", then this string can be split into 6 different ways as [11, 37, 3),
[113, 7, 3), [11, 3, 73), [11, 37, 3), (113, 73) and [11, 373) where each one of them contains only
prime numbers.

Input Format For Custom Testing
The first and only line contains the string, s.
Sample Case 0

Sample Input

For Custom Testing
3175

Sample Output Explanation
The 3 ways to split this string into prime numbers are (31, 7,5), (3, 17, 5), (317,5)
'''

class Solution:
    def countNumberOfWays(self, input):

        def isPrime(number):
            nonlocal mapping
            if number in mapping:
                return mapping[number]
            if number <= 1:
                return False
            if number == 2:
                return True
            if number % 2 == 0:
                return False
            for i in range(3, number//2, 2):
                if number % i == 0:
                    return False
            mapping[number] = True
            return True

        def numOfWays(input, output, result):
            if len(input) == 0:
                output.append(result)
                return
            for i in range(0, len(input)):
                current = int(input[:i+1])
                if isPrime(current):
                    result.append(current)
                    numOfWays(input[i+1:], output, result)
                    result.pop()


        result = []
        output = []
        mapping = {}
        numOfWays(input, output, result)
        return len(output)

input = "3175"
print(Solution.countNumberOfWays((), input))

input = "11373"
print(Solution.countNumberOfWays((), input))