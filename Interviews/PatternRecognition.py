'''Pattern Recognition 
Given a pattern as the first argument and a string of blobs split by | show the number of times the pattern is 
present in each blob and the total number of matches.

Input:
The input consists of the pattern (“bc” in the example) which is separated by a semicolon followed by a list of blobs 
(“bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32” in the example). Example input: bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32

Output:
The output should consist of the number of occurrences of the pattern per blob (separated by |). Additionally, 
the final entry should be the summation of all the occurrences (also separated by |).

Example output: 3|2|1|2|8 where ‘bc’ was repeated 3 times, 2 times, 1 time, 2 times in the 4 blobs passed in. 
And 8 is the summation of all the occurrences (3+2+1+2 = 8)'''

import re
def patternRecognition(string):

    def findPattern(pattern, item):
        nonlocal totalCount
        count = 0
        for i in range(len(item)):
            if pattern == item[i:i+len(pattern)]:
                count += 1
        totalCount += count
        return count

    delimeter, items = string.split(";", 1)
    if delimeter == '':
        output = [0] * (len(items.split('|')) + 1)
        return '|'.join([str(count) for count in output])
    
    totalCount = 0
    pattern = delimeter
    counts = [findPattern(pattern, item) for item in items.split('|')]
    counts.append(totalCount)
    return '|'.join([str(count) for count in counts])

string = "bc;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32"
patternRecognition(string) # output 3|2|1|2|8
patternRecognition('aa;aaaakjlhaa|aaadsaaa|easaaad|sa') # output 4|4|2|0|10
patternRecognition('b;bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32') # output 4|2|3|2|11
patternRecognition(';bcdefbcbebc|abcdebcfgsdf|cbdbesfbcy|1bcdef23423bc32') # output 0|0|0|0|0