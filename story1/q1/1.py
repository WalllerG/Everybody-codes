import re
from collections import deque

with open('input.txt')as f:
    data = f.read().splitlines()

INIT = 1
result = 0

def eni(n, exp, mod):
    remainders = deque()
    score = INIT
    for _ in range(exp):
        score = score * n % mod
        remainders.appendleft(score)
    return int("".join(map(str, remainders)))

for line in data:
    A, B, C, X, Y, Z, M = list(map(int, re.findall(r"\d+",line)))
    result = max(result, eni(A, X, M) +  eni(B, Y, M) +  eni(C, Z, M))
print(result)