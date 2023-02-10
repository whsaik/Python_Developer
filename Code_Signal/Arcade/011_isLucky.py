# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# solution(n) = true;
# For n = 239017, the output should be
# solution(n) = false

def solution(n):
    counts = 0
    a = str(n)
    for i in range(len(a)):
        if i < len(a)/2 :
            counts += int(a[i])
            
        else:
            counts -= int(a[i])
            
    if counts == 0:
        return True

    return False
