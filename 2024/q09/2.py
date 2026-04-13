from z3 import *
with open('input.txt')as f:
    data = [int(line) for line in f.read().splitlines()]

stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
ans = 0

for num in data:
    
    solver = Optimize()
    vars = [Int(f"x{i}") for i in range(10)]
    for v in vars:
        solver.add(v >= 0)
    sum = Sum(var * stamp for var, stamp in zip(vars, stamps))
    solver.add(sum == num)
    count = Sum(var for var in vars)
    solver.minimize(count)
    solver.check()
    m = solver.model()
    
    for var in vars:
        ans += m[var].as_long()
    
print(ans)