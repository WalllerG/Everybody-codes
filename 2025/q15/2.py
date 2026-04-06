import heapq
with open('input.txt')as f:
    data = f.read().split(',')
walls = [(0,0)]
directions = [(0,1),(1,0),(0,-1),(-1,0)]
dir_index = 3
cur = (0, 0)
for rule in data:
    direction, steps = rule[0], rule[1:]
    if direction == 'L':
        dir_index = (dir_index - 1) % 4
        dx, dy = directions[dir_index]
        for i in range(int(steps)):
            x, y = cur
            nx, ny =  x + dx, y + dy
            walls.append((nx, ny))
            cur = (nx, ny)
    else:
        dir_index = (dir_index + 1) % 4
        dx, dy = directions[dir_index]
        for i in range(int(steps)):
            x, y = cur
            nx, ny =  x + dx, y + dy
            walls.append((nx, ny))
            cur = (nx, ny)
end = walls[-1]
walls = walls[1:-1]
walls = set(walls)
def solve():
    sr = min(walls, key=lambda x:x[0])[0]
    r = max(walls, key=lambda x:x[0])[0]
    sc = min(walls, key=lambda x:x[1])[1]
    c = max(walls, key=lambda x:x[1])[1]
    
    queue = [(0, 0, 0)]
    seen = set()
    while queue:
        step, x, y = heapq.heappop(queue)
        if (x, y) == end:
            return step
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in walls and (nx, ny) not in seen and sr <= nx < r and sc <= ny < c:
                heapq.heappush(queue, (step+1, nx, ny))
                seen.add((nx, ny))
    
print(solve())