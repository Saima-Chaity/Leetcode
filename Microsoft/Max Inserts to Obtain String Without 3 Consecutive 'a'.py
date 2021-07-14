'''Max Inserts to Obtain String Without 3 Consecutive 'a'

Given a string S, returns the maximum number of letters a that can be inserted into S (including at the front
and end of S) so that the resulting string doesn’t contain three consecutive letters a. If string S already
contains the substring aaa, then your function should return -1.

Example 1:
Input: aabab
Output: 3
Explanation:
A string aabaabaa can be made

Example 2:
Input: dog
Output: 8
Explanation:
A string aadaaoaagaa can be made'''


'''If N is number of characters in the given string and all characters are not A we can insert into this string 
2 * (N + 1) characters, because we can insert two As between of each two characters in the string and two As to 
the begin and to the end of the string. Thus, in order to solve this task we need to count all non A chars.
When we will know this number it will be easy to calculate how many As we can insert. This number will be 
2 * (number of possible places to insert + 1) — number of found As.
In other words 2 * (N + 1) — (N — number of As);'''

def max_inserts(s: str) -> int:
    a_count = 0
    others_count = 0

    for i in range(len(s)):
        if s[i] == 'a':
            a_count += 1
        else:
            a_count = 0
            others_count += 1

        if a_count >= 3:
            return -1

    return 2 * (others_count + 1) - (len(s) - others_count)
