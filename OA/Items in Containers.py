'''Items in Containers

A company would like to know how much inventory exists in their closed inventory compartments.

Gwen a string s consisting of items as * and closed compartments as an open and close |, an array of starting indices
startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments within
the substring between the two indices, inclusive.

An item is represented as an asterisk ( * = ascii decimal 42)
A compartment is represented as a pair of pipes that may or may not have items between them ( | = ascii decimal 124).
Example 1:
Input: s = |**|*|*, startIndices = [1, 1], endIndices = [5, 6]
Output: [2, 3]
Explanation:
The string has a total of 2 closed compartments, one with 2 items and one with 1 item.

For the first pair of indices, (1, 5), the substring |**|*. There are 2 items in a compartment.

For the second pair of indices, (1, 6), the substring is |**|*| and there are 2 + 1 = 3 items in compartments.

Both of the answers are returned in an array, [2, 3]

Example 2:
Input: s = *|*|, startIndices = [1], endIndices = [3]
Output: []
Explanation:
the substring from index = 1 to index = 3 is *|*. There is no compartments in this string.

Constraints:
1 <= m, n <= 10^5
1 <= startIndices[i] <= endIndices[i] <= n
Each character or s is either * or |
'''

class Solution:
    def itemsInContainer(self, s, startIndexes, endIndexes):

        def getClosedItems(substring):
            startIndex = 0
            endIndex = 0
            startFound = False
            endFound = False
            starCount = 0

            for i in range(len(substring)):
                if substring[i] == "|" and not startFound:
                    startIndex = i
                    startFound = True
                    break

            for i in range(len(substring)-1, -1, -1):
                if substring[i] == "|" and not endFound:
                    endIndex = i
                    endFound = True
                    break

            if startFound and endFound:
                for i in range(startIndex+1, endIndex):
                    if substring[i] == "*":
                        starCount += 1
            return starCount

        i = 0
        j = 0
        output = []
        while i < len(startIndexes) and j < len(endIndexes):
            start = startIndexes[i]
            end = endIndexes[j]
            substring = s[start-1:end]
            result = getClosedItems(substring)
            if result:
                output.append(result)
            i += 1
            j += 1

        return output

s = "|**|*|*"
startIndices = [1, 1, 2]
endIndices = [5, 6, 6]
print(Solution.itemsInContainer((), s, startIndices, endIndices))

s = "*|*|"
startIndices = [1]
endIndices = [3]
print(Solution.itemsInContainer((), s, startIndices, endIndices))