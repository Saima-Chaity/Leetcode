'''Design File System - https://leetcode.com/problems/design-file-system/

You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English
letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true.
Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.

Example 1:

Input:
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output:
[null,true,1]
Explanation:
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
'''


class FileSystem:

    def __init__(self):
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if path == "/" or len(path) == 0 or path in self.paths:
            return False
        parent = path[:path.rfind("/")]
        if len(parent) > 1 and parent not in self.paths:
            return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.paths:
            return self.paths[path]
        return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

class FileSystem:

    def __init__(self):
        self.trie = {}

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split("/")[1:]
        t = self.trie
        for index, pathName in enumerate(paths, 1):
            if pathName not in t:
                if index == len(paths):
                    t[pathName] = {}
                else:
                    return False
            t = t[pathName]

        if '#' in t:
            return False

        t['#'] = value
        return True

    def get(self, path: str) -> int:
        paths = path.split("/")[1:]
        t = self.trie
        for pathName in paths:
            if pathName not in t:
                return -1
            t = t[pathName]
        return t['#']

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)