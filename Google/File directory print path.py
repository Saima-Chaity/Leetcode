'''first question: given a file directory as a string in following way, print the path as a tree.

input: /a/b/c

output:
a
-b
--c
'-' corresponds to a tab

question 2: given a list of strings, having same format as question 1. Now print the whole file structure.
if there are multiple files or directories in a directory, then order them based on the order in the input.

input:
'/a/c/ac', 'a/b/ab', 'b/c/bc', 'a/c/ac2'

output:
a
-c
--ac
--ac2
-b
--ab
b
-c
--bc
'''

class Solution:
    def __init__(self):
        self.trie = {}

    def add(self, children, t):
        for char in children:
            if char not in t:
                t[char] = {}
            t = t[char]

    def create_tree(self, path):
        t = self.trie
        for files in path:
            if not path:
                continue
            if files[0] == "/":
                files = files[1:]
            splited_file = files.split('/')
            self.add(splited_file, t)

    def print_path(self, path, depth=0):
        if not path:
            return
        for node in path.keys():
            print("-" * depth + str(node))
            self.print_path(path[node], depth+1)

    def get_directory_path(self, path):
        self.create_tree(path)
        t = self.trie
        self.print_path(t)

solution = Solution()
print(solution.get_directory_path(['/a/c/ac', 'a/b/ab', 'b/c/bc', 'a/c/ac2']))
