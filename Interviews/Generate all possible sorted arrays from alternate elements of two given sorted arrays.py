'''
Generate all possible sorted arrays from alternate elements of two given sorted arrays
Given two sorted arrays A and B, generate all possible arrays such that first element is taken from A then from B then
from A and so on in increasing order till the arrays exhausted. The generated arrays should end with an element from B.

For Example

A = {10, 15, 25}
B = {1, 5, 20, 30}

The resulting arrays are:
  10 20
  10 20 25 30
  10 30
  15 20
  15 20 25 30
  15 30
  25 30
'''

def printArr(arr, n):
    for i in range(n):
        print(arr[i], " ", end="")
    print()

def generateUtil(A, B, C, i, j, m, n, len, flag, output):

    if flag:
        if len:
            output.append(C[:len+1])
            printArr(C, len + 1)

        for k in range(i, m):
            # this only works for first call
            if not len:
                C[len] = A[k]
                generateUtil(A, B, C, k+1, j, m, n, len, not flag, output)
            else:
                if A[k] > C[len]:
                    C[len+1] = A[k]
                    generateUtil(A, B, C, k + 1, j, m, n, len + 1, not flag, output)
    else:
        for h in range(j, n):
            if B[h] > C[len]:
                C[len + 1] = B[h]
                generateUtil(A, B, C, i, h+1, m, n, len + 1, not flag, output)
    return output

def generate(A, B, m, n):
    C = []  # output array
    for i in range(m + n + 1):
        C.append(0)
    output = []
    generateUtil(A, B, C, 0, 0, m, n, 0, True, output)
    print(output)


# Driver program

A = [10, 15, 25]
B = [5, 20, 30]
n = len(A)
m = len(B)

generate(A, B, n, m)
