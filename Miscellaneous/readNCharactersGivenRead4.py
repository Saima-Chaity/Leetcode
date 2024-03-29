# Read N Characters Given Read4 - https://leetcode.com/problems/read-n-characters-given-read4/

'''Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf
    Returns:    int

Note: buf[] is destination not source, the results from read4 will be copied to buf[]
Below is a high level example of how read4 works:

File file("abcdefghijk"); // File is "abcdefghijk", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf); // read4 returns 4. Now buf = "efgh", fp points to 'i'
read4(buf); // read4 returns 3. Now buf = "ijk", fp points to end of file


Method read:

By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer
array buf. Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]


Example 1:

Input: file = "abc", n = 4
Output: 3
Explanation: After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so
return 3. Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the
results to.'''

"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

from collections import deque

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = deque()

    def read(self, buf: List[str], n: int) -> int:
        i = 0
        buf4 = [''] * 4
        while i < n:
            if self.q:
                buf[i] = self.q.popleft()
                i += 1
            else:
                readFile = read4(buf4)
                if readFile == 0:
                    break
                self.q.extend(buf4[:readFile])
        return i


# Read N Characters Given Read4 II - Call multiple times - https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
from collections import deque
class Solution:
    def __init__(self):
        self.q = deque()
        self.buf4 = [''] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.popleft()
                i += 1
            else:
                readFile = read4(self.buf4)
                if readFile == 0:
                    break
                self.q.extend(self.buf4[:readFile])
        return i