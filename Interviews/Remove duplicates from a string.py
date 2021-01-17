'''Remove duplicates from a string
Given a string str of lowercase characters, the task is to remove duplicates and
return a resultant string without modifying the order of characters in the original string.

Examples:

Input: str = "geeksforgeeks"
Output: geksfor

Input: str = "characters"
Output: chartes'''


def removeDuplicatesFromString(string):
    # Table to keep track of visited
    # characters
    table = [0 for i in range(256)]

    # To keep track of end index
    # of resultant string
    endIndex = 0
    string = list(string)

    for i in range(len(string)):
        if (table[ord(string[i])] == 0):
            table[ord(string[i])] = -1
            string[endIndex] = string[i]
            endIndex += 1

    return "".join(string[:endIndex])


# Driver code
if __name__ == '__main__':
    temp = "geeksforgeeks"

    print(removeDuplicatesFromString(temp))
