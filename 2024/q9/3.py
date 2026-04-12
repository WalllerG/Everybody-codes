from z3 import *
with open('input.txt')as f:
    data = [int(line) for line in f.read().splitlines()]

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
ans = 0

def solve(target):
    re = 0
    solver = Optimize()
    x_vars = [Int(f"x{i}") for i in range(len(stamps))]
    y_vars = [Int(f"y{i}") for i in range(len(stamps))]
    x = Int('x')
    y = Int('y')
    for var in x_vars:
        solver.add(var >= 0)
    for var in y_vars:
        solver.add(var >= 0)
    solver.add(x + y == target)
    solver.add(abs(x-y) <= 100)
    x_sum = Sum(var * stamp for var, stamp in zip(x_vars, stamps))
    y_sum = Sum(var * stamp for var, stamp in zip(y_vars, stamps))
    solver.add(x_sum == x)
    solver.add(y_sum == y)
    count = Sum(var for var in x_vars) + Sum(var for var in y_vars)
    solver.minimize(count)
    solver.check()
    m = solver.model()
    for var in x_vars:
        re += m[var].as_long()
    for var in y_vars:
        re += m[var].as_long()
    return re

for num in data:
    ans += solve(num)
print(ans)