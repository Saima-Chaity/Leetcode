# Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/
'''Given a string containing only digits, restore it by returning all possible valid IP
address combinations.
A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated
by single points.

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]'''

class Solution:
    def restoreIpAddresses(self, s):

        self.output = set()
        def getValidIpAddresses(s, path, index):
            if index == 4:
                if not s:
                    path = path[:-1]
                    self.output.add(path)
                return
            for i in range(1, 4):
                # the digits we choose should no more than the length of s
                if i <= len(s):
                    # choose one digit
                    if i == 1:
                        getValidIpAddresses(s[i:], path + s[:i] + ".", index + 1)
                    # choose two digits, the first one should not be "0"
                    elif i == 2 and s[0] != '0':
                        getValidIpAddresses(s[i:], path + s[:i] + ".", index + 1)
                    # choose three digits, the first one should not be "0", and should less than 256
                    elif i == 3 and s[0] != '0' and int(s[:i]) <= 255:
                        getValidIpAddresses(s[i:], path + s[:i] + ".", index + 1)

        getValidIpAddresses(s, "", 0)
        return list(self.output)

