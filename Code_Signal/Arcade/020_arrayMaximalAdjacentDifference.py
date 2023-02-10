# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

# Example

# For inputArray = [2, 4, 1, 0], the output should be
# solution(inputArray) = 3.

def solution(inputArray):
    d = abs(inputArray[0] - inputArray[1])
    for i in range(len(inputArray)-1):
        d2 = abs(inputArray[i+1] - inputArray[i])
        if d2 > d:
            d = d2
    
    return d   
