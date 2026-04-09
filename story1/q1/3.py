import re
from collections import deque
with open('input.txt')as f:
    data = f.read().splitlines()

INIT = 1
result = 0

def eni(n, exp, mod):
    total = 0
    score = INIT
    pattern = {}
    for i in range(exp):
        score = score * n % mod
        total += score
        if score not in pattern:
            pattern[score] = i
        else:
            vals = list(pattern.keys())
            starting_index = pattern[score]
            if starting_index == 0:
                leftover = exp % len(pattern)
                return exp // len(pattern) * sum(pattern.keys()) + sum(vals[x] for x in range(leftover))
            else:
                leftover = (exp-len(vals[:starting_index])) % len(vals[starting_index:])
                return (exp-len(vals[:starting_index])) // len(vals[starting_index:]) * sum(vals[starting_index:]) + sum(vals[starting_index:][x] for x in range(leftover)) + sum(vals[:starting_index])
    return total
    
for line in data:
    A, B, C, X, Y, Z, M = list(map(int, re.findall(r"\d+",line)))
    result = max(result, eni(A, X, M) +  eni(B, Y, M) +  eni(C, Z, M))
print(result)