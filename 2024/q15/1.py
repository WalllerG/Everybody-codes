import heapq
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]
    
H = set()
S = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i == 0 and grid[i][j] == '.':
            S = (i, j)
        elif grid[i][j] == 'H':
            H.add((i, j))
            
def bfs(sx, sy, ex, ey):
    queue = [(0, sx, sy)]
    seen = {(sx, sy):0}
    while queue:
        step, x, y = heapq.heappop(queue)
        if (x, y) == (ex, ey):
            return step
        for nx, ny in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
                if (nx, ny) not in seen or step + 1 < seen[(nx, ny)]:
                    heapq.heappush(queue, (step+1, nx, ny))
                    seen[(nx, ny)] = step + 1
    return -1

ans = 1000000
for h in H:
    ans = min(ans, bfs(S[0], S[1], h[0], h[1]) * 2)
print(ans)