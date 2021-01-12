# Find Common Characters - https://leetcode.com/problems/find-common-characters/
'''Given an array A of strings made only from lowercase letters, return a list of all characters that show 
up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all 
strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]'''

from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        firstWord = Counter(A[0])
        for word in A[1:]:
            temp = {}
            for char in word:
                if char in firstWord:
                    temp[char] = temp.get(char, 0) + 1
                    firstWord[char] -= 1
                    if firstWord[char] == 0:
                        del firstWord[char]
            firstWord = temp

        output = ""
        for char, freq in firstWord.items():
            output += char * freq
        return list(output)

#Using list
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        firstWord = list(A[0])
        for word in A[1:]:
            temp = []
            for char in word:
                if char in firstWord:
                    temp.append(char)
                    firstWord.remove(char)
            firstWord = temp
        return firstWord
