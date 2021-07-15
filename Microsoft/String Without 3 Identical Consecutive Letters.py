'''String Without 3 Identical Consecutive Letters

Given a string S having lowercase English letters, returns a string with no instances of three identical consecutive
letters, obtained from S by deleting the minimum possible number of letters.

Example 1:
Input: eedaaad
Output: eedaad
Explanation:
One occurrence of letter a is deleted.

Example 2:
Input: xxxtxxx
Output: xxtxx
Explanation:
Note that letter x can occur more than three times in the returned string if the occurrences are not consecutive.

Example 3:
Input: uuuuxaaaaxum
Output: uuxaaxum'''

def filter_string(s: str) -> str:
    output = s[0:2]
    for i in range(2, len(s)):
        if s[i] != s[i - 1] or s[i] != s[i - 2]:
            output += s[i]
    return output


# Another approach
def filter_string(s: str) -> str:
    count = 1
    result = s[0]

    for i in range(1, len(s)):
        # we met two the same letters increase the counter
        if s[i] == s[i - 1]:
            count += 1
        else:
            # if next letter is different drop the counter to 1
            count = 1

        if count <= 2:
            result += s[i]
    return result