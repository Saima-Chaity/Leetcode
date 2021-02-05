'''Given the first and the last word and followed by a list of words , print wether the
words comes before, after or inside the range of the first and the last word based on the following
order ' ' < A < a < B < b.... Z < z

input :

Apple Pie
Aa
Aq
Apple
Zefa

output:
before // since Aa < Apple
inside // since Aq > Aa && Aq < Pie
inisde // since Apple = Apple
after // since Zefa > Pie'''

class Solution:
    def lastAndFirstWord(self, words, firstWord, lastWord):

        wordList = words
        wordList.append(firstWord)
        wordList.append(lastWord)
        wordList.sort()

        indexOfFirstWord = wordList.index(firstWord)
        indexOfSecondWord = wordList.index(lastWord)

        beforeList = wordList[:indexOfFirstWord]
        insideList = wordList[indexOfFirstWord+1:indexOfSecondWord]
        afterList = wordList[indexOfSecondWord+1:]

        print(wordList)
        print(beforeList, insideList, afterList)

        for word in wordList:
            if word in beforeList:
                print("before " + word)
            elif word in insideList:
                print("inside " + word)
            elif word in afterList:
                print("after " + word)


words = ['AA', 'Aa', 'Aq', 'Apple', 'Zefa']
firstWord = 'Apple'
lastWord = 'Pie'
print(Solution.lastAndFirstWord((), words, firstWord, lastWord))

