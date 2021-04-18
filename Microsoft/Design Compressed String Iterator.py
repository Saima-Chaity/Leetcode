'''Design Compressed String Iterator - https://leetcode.com/problems/design-compressed-string-iterator/

Design and implement a data structure for a compressed string iterator. The given compressed string will be in the
form of each letter followed by a positive integer representing the number of this letter existing in the original
uncompressed string.

Implement the StringIterator class:

next() Returns the next character if the original string still has uncompressed characters, otherwise
returns a white space.
hasNext() Returns true if there is any letter needs to be uncompressed in the original string,
otherwise returns false.

Example 1:

Input
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
Output
[null, "L", "e", "e", "t", "C", "o", true, "d", true]

Explanation
StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // return "L"
stringIterator.next(); // return "e"
stringIterator.next(); // return "e"
stringIterator.next(); // return "t"
stringIterator.next(); // return "C"
stringIterator.next(); // return "o"
stringIterator.hasNext(); // return True
stringIterator.next(); // return "d"
stringIterator.hasNext(); // return True'''


class StringIterator:

    def __init__(self, compressedString: str):
        self.strs = compressedString
        self.current_count = 0
        self.current_letter = None
        self.index = 0

    def next(self) -> str:
        if self.hasNext():
            value = self.current_letter
            self.current_count -= 1
            if self.current_count == 0:
                self.current_letter = None
            return value
        return " "

    def hasNext(self) -> bool:
        if self.index >= len(self.strs) and self.current_letter is None:
            return False

        if self.current_letter == None:
            self.current_letter = self.strs[self.index]
            self.index += 1
            num = 0
            while self.index < len(self.strs) and self.strs[self.index].isdigit():
                num = num * 10 + int(self.strs[self.index])
                self.index += 1
            self.current_count = num
        return True

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()