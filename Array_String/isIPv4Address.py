'''An IP address is a numerical label assigned to each device (e.g., computer, printer)
participating in a computer network that uses the Internet Protocol for communication.
There are two versions of the Internet protocol, and thus two versions of addresses.
One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.'''


def isIPv4Address(inputString):
    if len(inputString) < 4:
        return False

    dotCounts = 0
    for index, char in enumerate(inputString):
        if char == ".":
            dotCounts += 1
        if char.isalpha() or (char == "." and index == 0):
            return False

    if dotCounts > 3:
        return False

    splitedInputString = inputString.split(".")

    count = 0
    for item in splitedInputString:
        if item == "." or item == "" or int(item) < 0 or int(item) > 255:
            return False
        elif len(item) == 2 and (item[0] == '0' or count >= 1):
            return False
        elif len(item) == 2:
            count += 1
    return True


