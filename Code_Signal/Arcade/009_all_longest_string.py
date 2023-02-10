# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# solution(inputArray) = ["aba", "vcd", "aba"].

def solution(inputArray):
    a = 0
    results = []
    for i in inputArray:
        n = len(i)
        if n > a:
            a = n
            
    for i in inputArray:
        n = len(i)
        if n == a:
            results.append(i)
            
    return results
