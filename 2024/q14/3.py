import heapq
with open('input.txt')as f:
    data = f.read().splitlines()
   
total = set()
leaves = set()
ans = float('inf')

for line in data:
    s = (0,0,0)
    seen = set()
    for op in line.split(','):
        rule, steps = op[0], int(op[1:])
        if rule == 'D':
            for i in range(1, steps+1):
                s = s[0], s[1] - 1, s[2]
                seen.add(s)
        elif rule == 'U':
            for i in range(1, steps+1):
                s = s[0], s[1] + 1, s[2]
                seen.add(s)
        elif rule == 'R':
            for i in range(1, steps+1):
                s = s[0] + 1, s[1], s[2]
                seen.add(s)
        elif rule == 'L':
            for i in range(1, steps+1):
                s = s[0] - 1, s[1], s[2]
                seen.add(s)
        elif rule == 'F':
            for i in range(1, steps+1):
                s = s[0], s[1], s[2] + 1
                seen.add(s)
        elif rule == 'B':
            for i in range(1, steps+1):
                s = s[0], s[1], s[2] - 1
                seen.add(s)
    leaves.add(s)
    total |= seen

def bfs(sx, sy, sz, ex, ey, ez):
    queue = [(0, sx, sy, sz)]
    seen = {(sx, sy, sz)}
    while queue:
        step, x, y, z = heapq.heappop(queue)
        if (x, y, z) == (ex, ey, ez):
            return step
        for nx, ny, nz in [(x+1, y, z),(x-1, y, z),(x, y+1, z),(x, y-1, z),(x, y, z+1),(x, y, z-1)]:
            if (nx, ny, nz) in total:
                if (nx, ny, nz) not in seen:
                    heapq.heappush(queue, (step+1, nx, ny, nz))
                    seen.add((nx, ny, nz))
    return -1
            
for s in range(1, 106):
    x, y, z = (0, s, 0)
    levels = sum(bfs(x, y, z, a, b, c) for a, b, c in leaves)
    ans = min(ans, levels)
        
print(ans)