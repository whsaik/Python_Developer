# Some people are standing in a row in a park. There are trees between them which cannot be moved. 
# Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

def solution(a):
    l1 = []
    n = len(a)
    for i in range(n):
        if a[i] == -1:
            continue
        else:
            l1.append(a[i])
            
    l1.sort()
    
    for i in range(n):
        if a[i] == -1:
            continue
        else:
            a[i] = l1[0]
            l1.pop(0)
    
    return a
