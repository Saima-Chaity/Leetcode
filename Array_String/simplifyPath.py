# Simplify Path - https://leetcode.com/problems/simplify-path/
'''Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the
directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between
two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path
must be the shortest string representing the absolute path.

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
'''


class Solution:
    def simplifyPath(self, path: str) -> str:

        if not path:
            return ""

        stack = []
        for portion in path.split("/"):
            if portion == "..":
                if len(stack) > 0:
                    stack.pop()
            elif portion == "." or not portion:
                continue
            else:
                stack.append(portion)

        canonicalPath = "/" + "/".join(stack)
        return canonicalPath