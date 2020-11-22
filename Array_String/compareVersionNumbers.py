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

        def getNextChunk(pointer, version_length, version):
            if pointer > version_length - 1:  # if pointer is set to the end of string return 0
                return pointer, 0

            pointer_end = pointer
            while pointer_end < version_length and version[pointer_end] != ".":
                pointer_end += 1
            number = int(version[pointer:pointer_end]) if pointer_end != version_length - 1 else \
                    version[pointer:version_length]
            pointer = pointer_end + 1  # beginning of next chunk
            return pointer, number

        version1_length = len(version1)
        version2_length = len(version2)
        pointer1 = pointer2 = 0

        while pointer1 < version1_length or pointer2 < version2_length:
            pointer1, version1_char = getNextChunk(pointer1, version1_length, version1)
            pointer2, version2_char = getNextChunk(pointer2, version2_length, version2)
            if version1_char != version2_char:
                return 1 if version1_char > version2_char else -1
        return 0


# Split + Parse, Two Pass
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        version1 = version1.split(".")
        version2 = version2.split(".")

        for i in range(max(len(version1), len(version2))):

            version1_char = int(version1[i]) if i < len(version1) else 0
            version2_char = int(version2[i]) if i < len(version2) else 0

            if version1_char != version2_char:
                return 1 if version1_char > version2_char else -1
        return 0