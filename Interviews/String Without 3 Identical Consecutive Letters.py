'''String Without 3 Identical Consecutive Letters
Given a string S consisting of N letters a and b. In one move you can replace one
letter by the other (a by b or b by a).

Write a function solution that given such a string S, returns the minimum number of
moves required to obtain a string containing no instances of three identical consecutive letters.

Example 1:

Input: "baaaaa"
Output: 1
Explanation: The string without three identical consecutive letters which can be obtained is one move is "baabaa".
Example 2:

Input: "baaabbaabbba"
Output: 2
Explanation: There are four valid strings obtainable in two moves, for example "bbaabbaabbaa".
Example 3:

Input: "baabab"
Ouput: 0
'''

def getCount(s):
    count = 0
    i = 0
    s = list(s)
    while i < len(s) - 2:
        if s[i] == s[i + 1] and s[i] == s[i + 2]:
            s[i+2] = " "
            count += 1
            i += 1
        else:
            i += 1
    print(count, s)
    return count

getCount('baaaaa') #output 1
getCount('baaabbaabbba') #output 2
getCount('baabab') #output 0
