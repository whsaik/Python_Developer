# You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. 
# Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

# Example

# For inputArray = [1, 1, 1], the output should be
# solution(inputArray) = 3.

def solution(inputArray):
    counter = 0
    for i in range(len(inputArray)-1):
        while inputArray[i+1] <= inputArray[i]:
            diff = abs(inputArray[i+1] - inputArray[i]) + 1
            inputArray[i+1] += diff
            counter += diff
    
    return counter
