from collections import deque
with open('input.txt')as f:
    data = f.read().splitlines()
grid = [list(line) for line in data]
center = ()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            center = (i, j)

def draw(radius):
    queue = deque([center])
    seen = {(center)}
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if (abs(nx - center[0]) * abs(nx - center[0]) + abs(ny - center[1]) * abs(ny - center[1])) <= radius * radius and (nx, ny) not in seen:
                    queue.append((nx, ny))
                    seen.add((nx, ny))
    return seen

possible = {}
r = 1
while True:
    bigger = draw(r+1)
    smaller = draw(r)
    re = bigger - smaller
    val = sum(int(grid[x][y]) for x, y in re)
    possible[val] = r+1
    r += 1
    print(max(possible.keys()) * possible[max(possible.keys())])