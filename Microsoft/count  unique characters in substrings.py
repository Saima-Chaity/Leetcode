'''count  unique characters in substrings

Given a string S, you need to count all the unique characters for substrings of the given string.

Example:

S='aabb'

output=14

a 1
aa 1
aab 2
aabb 2
a 1
ab 2
abb 2
b 1
bb 1
b 1

S="abc"
output=10

Expected time complexity O(n)'''

'''
Think about string "XAXAXXAX" and focus on making the second "A" a unique character.
We can take "XA(XAXX)AX" and between "()" is our substring.
We can see here, to make the second "A" counted as a uniq character, we need to:

insert "(" somewhere between the first and second A
insert ")" somewhere between the second and third A
For step 1 we have "A(XA" and "AX(A", 2 possibility.
For step 2 we have "A)XXA", "AX)XA" and "AXX)A", 3 possibilities.

So there are in total 2 * 3 = 6 ways to make the second A a unique character in a substring.
In other words, there are only 6 substring, in which this A contribute 1 point as unique string.

Instead of counting all unique characters and struggling with all possible substrings,
we can count for every char in S, how many ways to be found as a unique char.
We count and sum, and it will be out answer.


Explanation
index[26][2] record last two occurrence index for every upper characters.
Initialise all values in index to -1.
Loop on string S, for every character c, update its last two occurrence index to index[c].
Count when loop. For example, if "A" appears twice at index 3, 6, 9 seperately, we need to count:
For the first "A": (6-3) * (3-(-1))"
For the second "A": (9-6) * (6-3)"
For the third "A": (N-9) * (9-6)"

Complexity
One pass, time complexity O(N).
Space complexity O(1).

One pass, time complexity O(N).
Space complexity O(1).'''

import string
class Solution:
    def uniqueCharacters(self, S):
        index = {c: [-1, -1] for c in string.ascii_letters}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10 ** 9 + 7)


# Space 0(n)
from collections import defaultdict
class Solution:
    def uniqueLetterString(self, S):

        indexes = defaultdict(list)
        for index, char in enumerate(S):
            indexes[char].append(index)

        count = 0
        for item in indexes.values():
            current = [-1] + item + [len(S)]
            for i in range(1, len(current) - 1):
                count += (current[i] - current[i - 1]) * (current[i + 1] - current[i])
        return count % (10 ** 9 + 7)

S='aabb'
print(Solution.uniqueLetterString((), S))


# Another approach - time complexity 0(n^2)
class Solution:
    def uniqueLetterString(self, S):

        count = 0
        for i in range(len(S)):
            left = i - 1
            right = i + 1
            while left >= 0 and S[left] != S[i]:
                left -= 1
            while right < len(S) and S[right] != S[i]:
                right += 1

            count += (right - i) * (i - left)
        return count % (10 ** 9 + 7)