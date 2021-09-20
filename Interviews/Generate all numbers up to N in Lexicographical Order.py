'''Generate all numbers up to N in Lexicographical Order
https://www.geeksforgeeks.org/generate-all-numbers-up-to-n-in-lexicographical-order/

Given an integer N, the task is to print all numbers up to N in Lexicographical order.

Examples:

Input: N = 15
Output:
1 10 11 12 13 14 15 2 3 4 5 6 7 8 9

Input: N = 19
Output:
1 10 11 12 13 14 15 16 17 18 19 2 3 4 5 6 7 8 9
'''

# Python program for the above approach
def printNumbers(n):
    result = []
    dfs(1, n, result)
    print(result)


def dfs(temp, n, sol):
    if temp > n:
        return n
    sol.append(temp)
    dfs(temp * 10, n, sol)
    if temp % 10 != 9:
        dfs(temp+1, n, sol)

n = 22
printNumbers(n)