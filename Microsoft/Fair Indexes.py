'''Fair Indexes

You are given two arrays A and B consisting of N integers each.

Index K is named fair if the four sums (A[0] + ... + A[K-1]), (A[k] + ... + A[N-1]), (B[0] + ... + B[k-1])
and (B[K] + ... + B[N-1]) are all equal. In other words, K is the index where the two arrays, A and B, can
be split (into two non-empty arrays each) in such a way that the sums of the resulting arrays' elements are equal.

write a function:

int fairIndexes(vector<int> &A, vector<int> &B);
which, given two arrays of integers A and B, returns the number of fair indexes.

Example 1:
Input: A = [4, -1, 0, 3], B = [-2, 5, 0, 3]
Output: 2
Explanation:
The fair indexes are 2 and 3. In both cases, the sums of elements the subarrays are equal to 3.

For index = 2;

4 + (-1) = 3; 0 + 3 = 3;

-2 + 5 = 3; 0 + 3 = 3;'''


def fairIndexes(A: [int], B: [int]) -> int:
    for i in range(1, len(A)):
        A[i] += A[i - 1]
        B[i] += B[i - 1]

    fairIndexes = 0
    for k in range(1, len(A)):
        left_A, right_A = A[k - 1], A[-1] - A[k - 1]
        left_B, right_B = B[k - 1], B[-1] - B[k - 1]

        if left_A == right_A == left_B == right_B:
            fairIndexes += 1
    return fairIndexes

print(fairIndexes([4, -1, 0, 3], [-2, 5, 0, 3]))