# An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network 
# that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. 
# One of them is the IPv4 address.

# Given a string, find out if it satisfies the IPv4 address naming rules.

# Example

# For inputString = "172.16.254.1", the output should be
# solution(inputString) = true;

# For inputString = "172.316.254.1", the output should be
# solution(inputString) = false.

# 316 is not in range [0, 255].

# For inputString = ".254.255.0", the output should be
# solution(inputString) = false.

# There is no first number.

def solution(inputString):
    check_list = inputString.split(".")
    if len(check_list) != 4:
        return False
    else:
        for i in check_list:
            if i.isdigit() == False or int(i) not in range(256) or len(i) != len(str(int(i))):
                return False         
    return True
