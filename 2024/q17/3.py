import heapq
from collections import defaultdict
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]
    
points = sorted(set((r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '*'), key=lambda x:(x[0], x[1]))
visited = set()
groups = defaultdict(int)
group_id = 0

for start_point in points:
    if start_point in visited:
        continue
    current_group_dist = 0
    q = [(0, start_point)]
    while q:
        dist, current_node = heapq.heappop(q)
        if current_node in visited:
            continue
        visited.add(current_node)
        current_group_dist += dist + 1
        for next_node in points:
            if next_node not in visited:
                d = abs(current_node[0] - next_node[0]) + abs(current_node[1] - next_node[1])
                if d < 6:
                    heapq.heappush(q, (d, next_node))
    groups[group_id] = current_group_dist
    group_id += 1

sort = sorted(list(groups.values()), reverse=True)
print(sort[0] * sort[1] * sort[2])