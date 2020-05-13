# Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/
'''Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of
the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example,
version number 3.4 has a revision number of 3 and 4 for its first and second level revision number.
Its third and fourth level revision number are both 0.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1'''


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def nextChunk(version, lengthOfV1, i):

            if i > lengthOfV1 - 1:
                return 0, i
            current = i
            while current < lengthOfV1 and version[current] != ".":
                current += 1
            number = int(version[i:current]) if current != lengthOfV1 - 1 else int(version[current:lengthOfV1])
            i = current + 1
            return number, i


        lengthOfV1 = len(version1)
        lengthOfV2 = len(version2)

        i = 0
        j = 0

        while i < lengthOfV1 or j < lengthOfV2:
            item1, i = nextChunk(version1, lengthOfV1, i)
            item2, j = nextChunk(version2, lengthOfV2, j)
            if item1 > item2:
                return 1
            elif item1 < item2:
                return -1
        return 0