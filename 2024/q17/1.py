import heapq
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]
    
points = sorted(set((r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '*'), key=lambda x:(x[0], x[1]))
ans = 0
visited = set()
min_heap = [(0, points[len(points) // 2])]
ans = 0

while len(visited) < len(points):
    dist, current_point = heapq.heappop(min_heap)
    if current_point in visited:
        continue
    ans += dist
    visited.add(current_point)
    for next_point in points:
        if next_point not in visited:
            d = abs(current_point[0] - next_point[0]) + abs(current_point[1] - next_point[1])
            heapq.heappush(min_heap, (d, next_point))
    
print(ans + len(points))