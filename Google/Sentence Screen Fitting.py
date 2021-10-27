'''Sentence Screen Fitting - https://leetcode.com/problems/sentence-screen-fitting/

Given a rows x cols screen and a sentence represented as a list of strings,
return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be
split into two lines. A single space must separate two consecutive words in a line.

Example 1:

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
Example 2:

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd-
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
'''


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        mapping = {}
        wordIndex = 0
        times = 0
        for row in range(rows):
            if wordIndex not in mapping:
                currentTimes = 0
                currentIndex = wordIndex
                col = 0
                while col < cols:
                    wordLength = len(sentence[currentIndex])
                    if wordLength <= cols - col:
                        col += wordLength + 1
                        if currentIndex == len(sentence) - 1:
                            currentTimes += 1
                        currentIndex = (currentIndex + 1) % len(sentence)
                    else:
                        break
                mapping[wordIndex] = (currentTimes, currentIndex)
                wordIndex = currentIndex
                times += currentTimes
            else:
                currentTimes, currentIndex = mapping[wordIndex]
                wordIndex = currentIndex
                times += currentTimes
        return times
