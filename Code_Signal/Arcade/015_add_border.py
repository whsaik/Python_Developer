# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

# Example

# For

# picture = ["abc",
#            "ded"]
# the output should be

# solution(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]

def solution(picture):
    pic_1 = list()
    for i in picture:
        a = "*" + i + "*"
        pic_1.append(a)
    
    n = len(pic_1[0])
    b = "*" * n
    pic_1.insert(0,b)
    pic_1.append(b)
    
    return pic_1   
