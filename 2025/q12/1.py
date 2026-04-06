with open('input.txt')as f:
    data = f.read().splitlines()
grid = [list(line) for line in data]
seen = {(0,0)}
queue = [(0,0)]
ans = 0
while queue:
    x, y = queue.pop(0)
    for dx, dy in [(-1, 0),(1, 0),(0,1),(0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and int(grid[nx][ny]) <= int(grid[x][y]) and (nx, ny) not in seen:
            queue.append((nx, ny))
            seen.add((nx, ny))
print(len(seen))