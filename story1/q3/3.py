import re
from z3 import *
with open('input.txt')as f:
    data = f.read().splitlines()

DAY = 0
solver = Solver()
day = Int('day')
def move(x, y, length):
    y_pos = [a if a > 0 else a + length for a in range(y,y-length,-1)]
    for i in range(len(y_pos)):
        if y_pos[i] == 1:
            solver.add(day % length == i)

for line in data:
    x, y = list(map(int, re.findall(r"\d+", line)))
    cycle_len = x + y - 1
    move(x, y, cycle_len)
    
solver.check()
m = solver.model()
print(m[day].as_long())