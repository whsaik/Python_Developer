# Given the string, check if it is a palindrome.
# A palindrome is...
# A string that doesn't changed when reversed (it reads the same backward and forward).

# Examples:

# "eye" is a palindrome
# "noon" is a palindrome
# "decaf faced" is a palindrome
# "taco cat" is not a palindrome (backwards it spells "tac ocat")
# "racecars" is not a palindrome (backwards it spells "sracecar")

# Example

# For inputString = "aabaa", the output should be
# solution(inputString) = true;
# For inputString = "abac", the output should be
# solution(inputString) = false;
# For inputString = "a", the output should be
# solution(inputString) = true.

def solution(inputString):
    a = list(inputString)
    b = a[::-1]
    if b == a:
        return True
    else:
        return False
