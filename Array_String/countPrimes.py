# Count Primes - https://leetcode.com/problems/count-primes/
'''Count the number of prime numbers less than a non-negative number, n.
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.'''

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        primes = [True] * n
        for i in range(2, n):
            if primes[i] == True:
                count += 1
                for j in range(i * i, n, i):
                    primes[j] = False
        return count
