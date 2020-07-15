# Fizz Buzz - https://leetcode.com/problems/fizz-buzz/
'''Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples
of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        result = []
        mapping = {3: 'Fizz', 5: 'Buzz', 15: 'FizzBuzz'}
        for num in range(1, n + 1):
            output = ""
            if num not in mapping:
                output = str(num)
            for key in mapping.keys():
                if num % key == 0:
                    output = mapping[key]
            result.append(output)
        return result


