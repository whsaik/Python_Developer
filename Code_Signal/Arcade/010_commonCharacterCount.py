# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# solution(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

def solution(s1, s2):
    d1 = dict()
    d2 = dict()
    results = []
    
    for i in range(len(s1)):
        if s1[i] not in d1:
            d1[s1[i]] = 1
        else:
            d1[s1[i]] += 1
            
    for i in range(len(s2)):
        if s2[i] not in d2:
            d2[s2[i]] = 1
        else:
            d2[s2[i]] += 1
            
    if len(d1) > len(d2):
        for k,v in d1.items():
            if k in d2 and v > d2[k]:
                results.append(d2[k])
            elif k in d2 and v <= d2[k]:
                results.append(v)
                
    elif len(d1) <= len(d2):
        for k,v in d2.items():
            if k in d1 and v > d1[k]:
                results.append(d1[k])
            elif k in d1 and v <= d1[k]:
                results.append(v)
    
    return sum(results)
