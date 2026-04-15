from collections import deque
from copy import deepcopy
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]
   
R = len(grid)
C = len(grid[0])
items = set()
sx, sy = None, None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i == 0 and grid[i][j] == '.':
            sx, sy = i, j
        elif grid[i][j] not in ('.', '#', '~'):
            items.add(grid[i][j])

queue = deque([(0, sx, sy, set())])
seen = set()
while queue:
    step, x, y, found = queue.popleft()
    key = (x, y, frozenset(found))
    if key in seen:
        continue
    seen.add(key)
    if found == items and x == sx and y == sy:
        print(step)
        break
    for nx, ny in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]:
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != "#" and grid[nx][ny] != "~":
            new_found = deepcopy(found)
            if grid[nx][ny] in items:
                new_found.add(grid[nx][ny])
            queue.append((step+1, nx, ny, new_found))

