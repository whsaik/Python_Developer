# Given a string, find out if its characters can be rearranged to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# solution(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.

def solution(inputString):
    lst = list(inputString)
    set_test = set(lst)
    d = dict()
    
    for i in set_test:
        d[i] = lst.count(i)
        
    counter = 0
    for k,v in d.items():
        if v%2 != 0:
            counter += 1
            
    if counter > 1:
        return False
    else:
        return True
