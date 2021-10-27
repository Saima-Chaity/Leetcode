'''Bulls and Cows - https://leetcode.com/problems/bulls-and-cows/

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is.
When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but
are located in the wrong position. Specifically, the non-bull digits in the guess that
could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows.
Note that both secret and guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
'''

from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        secret_counts = Counter(secret)
        bulls = cows = 0
        for index, char in enumerate(guess):
            if char in secret_counts:
                if char == secret[index]:
                    bulls += 1
                    cows -= int(secret_counts[char] <= 0)
                else:
                    cows += int(secret_counts[char] > 0)
                secret_counts[char] -= 1
        return "{}A{}B".format(bulls, cows)