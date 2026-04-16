from collections import deque
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]
    
trees = set((i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 'P')
points = set((i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == '.')
R = len(grid)
C = len(grid[0])
ans = float('inf')

def solve(S):
    found = set()
    queue = deque([(0, S[0], S[1])])
    seen = {S}
    total = 0
    while queue:
        time, x, y = queue.popleft()
        if (x, y) in trees:
            found.add((x, y))
            total += time
        if found == trees:
            return total
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = dx + x, dy + y
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#':
                if (nx, ny) not in seen:
                    seen.add((x, y))
                    queue.append((time+1, nx, ny))
    return -1

for p in points:
    ans = min(ans, solve(p))
print(ans)