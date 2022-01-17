'''Validate IP Address - https://leetcode.com/problems/validate-ip-address/

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or
"Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros.
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00"
and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case
English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid
IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
are invalid IPv6 addresses.

Example 1:

Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
'''

class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        allowed_char = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']

        def isIPV6(query_ip):
            splited_ip = query_ip.split(":")
            if len(splited_ip) != 8:
                return 'Neither'
            for ip in splited_ip:
                if not ip or len(ip) > 4:
                    return 'Neither'
                for char in ip:
                    if not char.isdigit() and char not in allowed_char:
                        return 'Neither'
            return 'IPv6'

        def isIPV4(query_ip):
            splited_ip = query_ip.split(".")
            if len(splited_ip) != 4:
                return 'Neither'
            for ip in splited_ip:
                if len(ip) > 1 and ip[0] == '0':
                    return 'Neither'
                if not ip or not ip.isdigit() or int(ip) < 0 or int(ip) > 255:
                    return 'Neither'
            return 'IPv4'

        if queryIP.count('.') == 3:
            return isIPV4(queryIP)
        if queryIP.count(':') == 7:
            return isIPV6(queryIP)
        else:
            return 'Neither'