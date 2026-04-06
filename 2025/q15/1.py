from collections import deque
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

def solve():
    queue = deque([(0, 0, 0)])
    seen = set()
    while queue:
        x, y, step = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in walls and (nx, ny) != walls[0] and (nx, ny) != walls[-1] and (nx, ny) not in seen:
                queue.append((nx, ny, step + 1))
                seen.add((nx, ny))
            if (nx, ny) == walls[-1]:
                return(step + 1)

print(solve())