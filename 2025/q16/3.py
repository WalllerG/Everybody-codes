from z3 import *
with open('input.txt')as f:
    data = [int(num) for num in f.read().split(',')]
spells = []
blocks = 202520252025000
while any(n > 0 for n in data):
    index = [n > 0 for n in data].index(True)
    spells.append(index + 1)
    for i in range(index, len(data), index+1):
        data[i] -= 1
solver = Optimize()
x = Int('x')
solver.add(x > 0)
used = [(x / num) for num in spells]
solver.add(Sum(used) <= blocks)
solver.maximize(x)
solver.check()
m = solver.model()
print(m[x].as_long())