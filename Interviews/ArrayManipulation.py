# Array Manipulation
# Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array 
# element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

# Example

# Queries are interpreted as follows:

#     a b k
#     1 5 3
#     4 8 7
#     6 9 1
# Add the values of  between the indices  and  inclusive:

# index->	 1 2 3  4  5 6 7 8 9 10
# 	[0,0,0, 0, 0,0,0,0,0, 0]
# 	[3,3,3, 3, 3,0,0,0,0, 0]
# 	[3,3,3,10,10,7,7,7,0, 0]
# 	[3,3,3,10,10,8,8,8,1, 0]
# The largest value is  after all operations are performed.

class Solution:
    def arrayManipulation(self, n, queries):
        arr = [0] *(n+1)
        maxSoFar = 0
        for query in queries:
            startIndex, endIndex, k = query[0], query[1], query[2]
            arr[startIndex-1] += k
            if endIndex < len(arr):
                arr[endIndex] -= k
        
        summation = 0
        for i in range(len(arr)):
            summation += arr[i]
            maxSoFar = max(maxSoFar, summation)
        return maxSoFar
