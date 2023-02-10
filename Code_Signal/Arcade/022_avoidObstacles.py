# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

# For example, if the jump is set to be 3, this means every jump should be the same which is 3.

# Find the minimal length of the jump enough to avoid all the obstacles.

# Example

# For inputArray = [5, 3, 6, 7, 9], the output should be
# solution(inputArray) = 4.

def solution(inputArray):
    step = 2 # step cannot be 1, it sure will step on obstacle
    inputArray.sort()
    
    while True:
        check_list = []
        for i in inputArray:
            a = i%step
            check_list.append(a) # check whether the quotient for obstacle for this step number is 0
            
        if 0 not in check_list: # no 0 meaning with this step number will not step on obstacle
            return step
        else:
            step += 1
