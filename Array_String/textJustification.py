# Text Justification - https://leetcode.com/problems/text-justification/
'''Given an array of words and a width maxWidth, format the text such that each line has
exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a
line do not divide evenly between words, the empty slots on the left will be assigned more spaces than
the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentWord = ""
        currentLength = 0
        output = []

        if len(words) == 0:
            return output

        for word in words:
            # First word
            if currentLength == 0:
                if len(word) <= maxWidth:
                    currentLength += len(word)
                    currentWord = word
            else:
                newLength = len(word) + currentLength + 1
                if newLength <= maxWidth:
                    currentLength = newLength
                    currentWord = currentWord + ' ' + word
                else:
                    result = self.fillOutSpace(currentWord, maxWidth)
                    output.append(result)
                    # Reset the currentWord and currentLength
                    currentWord = word
                    currentLength = len(word)
        # Last line
        if currentWord:
            diff = maxWidth - len(currentWord)
            lineWithSpace = currentWord + " " * diff
            output.append(lineWithSpace)
        return output

    def fillOutSpace(self, sentence, lineLength):
        diff = lineLength - len(sentence)
        separator = " "
        spaceCount = sentence.count(separator)
        if spaceCount > 0:
            multiplier = diff // spaceCount + 1
            # if the diff is too big, we need to evenly add the spaces, so replace each space with a multipler * space.
            if multiplier > 1:
                sentence = sentence.replace(separator, separator * multiplier)
                # New separator
                separator = separator * multiplier
                # The remainder is now the mod
                diff = diff % spaceCount

        while diff and " " in sentence:
            sentence = sentence.replace(separator, separator + " ", diff)
            diff = lineLength - len(sentence)

        if len(sentence) < lineLength:
            sentence = sentence + diff * ' '
        return sentence
