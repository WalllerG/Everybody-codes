from functools import cache
import sys
from collections import deque
sys.setrecursionlimit(100000)
with open('input.txt')as f:
    data = f.read().splitlines()
grid = [list(map(int, line)) for line in data]
blobs = {}
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) in blobs: continue
        blob = {(i, j)}
        queue = deque(blob)
        while len(queue) > 0:
            x, y = queue.popleft()
            for nx, ny in [(x-1, y),(x+1, y),(x, y-1),(x, y+1)]:
                if nx < 0 or nx >= len(grid): continue
                if ny < 0 or ny >= len(grid[0]): continue
                if grid[x][y] != grid[nx][ny]: continue
                if (nx, ny) in blob: continue
                blob.add((nx, ny))
                queue.append((nx, ny))
        for x, y in blob:
            blobs[(x, y)] = blob

@cache
def dfs(r, c):
    total = set(blobs[(r, c)])
    for cr, cc in list(total):
        for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
            if nr < 0 or nr >= len(grid): continue
            if nc < 0 or nc >= len(grid[nr]): continue
            if grid[nr][nc] >= grid[cr][cc]: continue
            total |= dfs(nr, nc)
    return total

total = set()
options = [dfs(x, y) for x in range(len(grid)) for y in range(len(grid[0]))]
for _ in range(3):
    best = max(options, key=lambda options: len(options - total))
    total |= best
print(len(total))