# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. 
# Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. 
# He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

# Example

# For statues = [6, 2, 3, 8], the output should be
# solution(statues) = 3.

# Ratiorg needs statues of sizes 4, 5 and 7.

def solution(statues):
    statues1 = []
    n = len(statues)
    
    for k in range(n):
        a = min(statues)
        statues1.append(a)
        statues.remove(a)
        
    count = 0

    for i in range(n-1):
        if statues1[i+1] - statues1[i] == 0:
            continue
        
        else:
            count = count + (statues1[i+1] - statues1[i] - 1)
            
    return count
