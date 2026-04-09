import re
from collections import deque
with open('input.txt')as f:
    data = f.read().splitlines()

INIT = 1
result = 0

def eni(n, exp, mod):
    remainders = deque()
    score = INIT
    pattern = {}
    for i in range(exp):
        score = score * n % mod
        remainders.appendleft(score)
        if len(remainders) == 6:
            remainders.pop()
            sequence = int("".join(map(str, remainders)))
            if sequence not in pattern:
                pattern[sequence] = i
            else:
                cycle_len = i - pattern[sequence]
                final_index = (exp - pattern[sequence] - 1)  % cycle_len
                return list(pattern.keys())[final_index]
    return int("".join(map(str, remainders)))

for line in data:
    A, B, C, X, Y, Z, M = list(map(int, re.findall(r"\d+",line)))
    result = max(result, eni(A, X, M) +  eni(B, Y, M) +  eni(C, Z, M))
print(result)