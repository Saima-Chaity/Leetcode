# Reverse Bits - https://leetcode.com/problems/reverse-bits/
'''Reverse bits of a given 32 bits unsigned integer.
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the
unsigned integer 43261596, so return 964176192 which its binary representation is
00111001011110000010100101000000.'''

class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n)[2:])  # removing "0b" prefix
        reversedStr = reversed(s)
        reversedBit = ''.join(reversedStr)

        for i in range(32 - len(reversedBit)):
            reversedBit += '0'
        return (int(reversedBit, 2))