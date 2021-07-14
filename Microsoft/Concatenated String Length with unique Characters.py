'''Concatenated String Length with unique Characters

Given an Array A consisting of N Strings, calculate the length of the longest string S such that:

S is a concatenation of some of the Strings from A.
every letter in S is different.
N is [1..8]
A consists of lowercase English letters
Sum of length of strings in A does not exceed 100.
Example 1:
Input: ["co","dil","ity"]
Output: 5
Explanation:
String S could be codil, dilco, coity, ityco

Example 2:
Input: ["abc","kkk","def","csv"]
Output: 6
Explanation:
Strings S could be abcdef , defabc, defcsv , csvdef

Example 3:
Input: ["abc","ade","akl"]
Output: 0
Explanation:
impossible to concatenate as letters wont be unique.'''


def max_length(arr: List[str]) -> int:
    result = 0

    def backTrack(path, index):
        nonlocal result
        if path and len(path) == len(set(path)):
            if path not in arr:
                result = max(result, len(path))

        for i in range(index, len(arr)):
            backTrack(path + arr[i], i + 1)

    backTrack("", 0)
    return result

print(max_length(["abc","kkk","def","csv"]))