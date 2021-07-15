'''Longest Substring Without Two Contiguous Occurrences of Letter

Given a string str containing only a and b, find the longest substring of str such that str does not
contain more than two contiguous occurrences of a and b.

Example 1:
Input: aabbaaaaabb
Output: aabbaa
Example 2:
Input: aabbaabbaabbaaa
Output: aabbaabbaabbaa'''

'''Time - 0(n) and space - 0(1)'''
def longestValidString(s) -> str:
    start = 0
    count = 1
    maxLength = 0
    start_position = 0

    for i in range(1, len(s)):
        # we met two the same letters increase the counter
        if s[i] == s[i - 1]:
            count += 1
        else:
            # if next letter is different drop the counter to 1
            count = 1

        if count <= 2:
            # if the sequence of different letters continuing
            if i - start + 1 > maxLength:
                maxLength = i - start + 1
                start_position = start
        else:
            # if the sequence of the same letters continuing, move the pointer to points to the last two
            # chars of this sequence and drop the count to 2
            count = 2
            start = i - 1
    return s[start_position:start_position+maxLength]

print(longestValidString("baaabbabbb"))
print(longestValidString("baaaabbbbbabbb"))