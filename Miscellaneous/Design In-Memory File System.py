# Design In-Memory File System - https://leetcode.com/problems/design-in-memory-file-system/
'''Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name.
If it is a directory path, return the list of file and directory names in this directory. Your output
(file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path.
If the middle directories in the path don't exist either, you should create them as well.
This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist,
you need to create that file containing given content. If the file already exists, you need to
append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

Example:

Input:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]'''

from collections import defaultdict
class FileSystem:

    def __init__(self):
        self.fileStructure = defaultdict(str)
        self.trie = {}

    def ls(self, path: str) -> List[str]:
        if len(path) == 1:
            return sorted(self.trie.keys())
        if path in self.fileStructure:
            return path.split("/")[-1:]
        else:
            t = self.trie
            splitedPath = path.split("/")
            for i in range(len(splitedPath)):
                current = splitedPath[i]
                if current == "":
                    continue
                if current in t:
                    t = t[current]
            return sorted(t.keys())

    def mkdir(self, path: str) -> None:
        t = self.trie
        if path not in self.fileStructure:
            splitedPath = path.split("/")
            for name in splitedPath:
                current = name
                if current == "":
                    continue
                if current not in t:
                    t[current] = {}
                t = t[current]

    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.fileStructure[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.fileStructure[filePath]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)