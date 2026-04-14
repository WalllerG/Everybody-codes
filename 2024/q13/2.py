import heapq
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]

s = None
e = None

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            s = (i, j)
        if grid[i][j] == 'E':
            e = (i, j)
            
def solve():
    queue = [(0, 0, s[0], s[1])]
    seen = {}
    while queue:
        time, level, x, y = heapq.heappop(queue)
        if (x, y) == e:
            return time
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
                new_time = None
                new_level = None
                if grid[nx][ny].isdigit():
                    x_time = time + 1 + abs(level - int(grid[nx][ny]))
                    y_time = time + 1 + level + 9 - int(grid[nx][ny]) + 1
                    z_time = time + 1 + 9 - level + int(grid[nx][ny]) + 1
                    new_time = min(x_time, y_time, z_time)
                    new_level = int(grid[nx][ny])
                else:
                    x_time = time + 1 + abs(level - 0)
                    y_time = time + 2 + level + 9 - 0
                    z_time = time + 2 + 9 - level + 0
                    new_time = min(x_time, y_time, z_time)
                    new_level = 0
                if (nx, ny) not in seen or new_time < seen[(nx, ny)]:
                    heapq.heappush(queue, (new_time, new_level, nx, ny))
                    seen[(nx, ny)] = new_time
    return -1

print(solve())