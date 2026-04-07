import heapq
from collections import defaultdict
with open('input.txt')as f:
    data = f.read().splitlines()
S = (0, 0)
walls = defaultdict(list)
for line in data:
    x, y, height = list(map(int, line.split(',')))
    walls[x].append((y-1, y + height))

def is_safe(nx, ny):
    if nx not in walls:
        return True
    return any(y_low < ny < y_high for y_low, y_high in walls[nx])

def bfs(target):
    queue = [(0, 0, 0)] 
    seen = {(0, 0): 0}
    while queue:
        flaps, x, y = heapq.heappop(queue)
        if x == target:
            return flaps
        for dx, dy in [(1, 1), (1, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= target and is_safe(nx, ny):
                new_flaps = flaps + 1 if dy == 1 else flaps
                if (nx, ny) not in seen or new_flaps < seen[(nx, ny)]:
                    seen[(nx, ny)] = new_flaps
                    heapq.heappush(queue, (new_flaps, nx, ny))
    return -1
print(bfs(1282))