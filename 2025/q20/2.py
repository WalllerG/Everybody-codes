import heapq
with open('/Users/walter/Desktop/everybody-codes/2025/q20/input.txt')as f:
    grid = [line for line in f.read().splitlines()]
trampolines = set()
S = ()
E = ()
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == 'T':
            trampolines.add((r, c))
        if char == 'S':
            S = (r, c)
        if char == 'E':
            E = (r, c)
            trampolines.add((r, c))
print(S, E)
def bfs(start, end):
    queue = [(0, start[0], start[1], 'down')]
    seen = {start : 0}
    while queue:
        step, x, y, face = heapq.heappop(queue)
        if (x, y) == end:
            return step
        if face == 'down':
            for (dx, dy) in [(-1,0),(0,1),(0,-1)]:
                nx, ny = x + dx, y + dy
                new_step = step + 1
                if (nx, ny) in trampolines:
                    if (nx, ny) not in seen or new_step < seen[(nx, ny)]:
                        heapq.heappush(queue, (new_step, nx, ny, 'up'))
                        seen[(nx, ny)] = new_step
        else:
            for (dx, dy) in [(1,0),(0,1),(0,-1)]:
                nx, ny = x + dx, y + dy
                new_step = step + 1
                if (nx, ny) in trampolines:
                    if (nx, ny) not in seen or new_step < seen[(nx, ny)]:
                        heapq.heappush(queue, (new_step, nx, ny, 'down'))
                        seen[(nx, ny)] = new_step
    return -1
print(bfs(S, E))