# Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/
'''Given a string containing only digits, restore it by returning all possible valid IP
address combinations.
A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated
by single points.

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        output = []
        def backTrack(s, path, index):
            if index == 4:
                if not s:
                    output.append(path[:-1])
                return
            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        backTrack(s[i:], path+s[:i]+".", index + 1)
                    if s[0] == "0":
                        break
                    
        backTrack(s, "", 0)
        return output
