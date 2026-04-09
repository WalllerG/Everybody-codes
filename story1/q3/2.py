import re
import math
with open('input.txt')as f:
    data = f.read().splitlines()

DAY = 0

def move(x, y, length):
    y_pos = [a if a > 0 else a + length for a in range(y,y-length,-1)]
    return y_pos[DAY % length]    

while True:
    days = []
    DAY += 1
    for line in data:
        x, y = list(map(int, re.findall(r"\d+", line)))
        cycle_len = x + y - 1
        days.append(move(x, y, cycle_len))
    if set(days) == {1}:
        print(DAY)
        break
