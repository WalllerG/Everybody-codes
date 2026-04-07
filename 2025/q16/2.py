import copy
import math
with open('input.txt')as f:
    data = [int(num) for num in f.read().split(',')]
ans = 1
cur = 1
while any(n > 0 for n in data):
    index = [n > 0 for n in data].index(True)
    ans *= index + 1
    for i in range(index, len(data), index+1):
        data[i] -= 1
print(ans)