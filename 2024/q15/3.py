from collections import deque, defaultdict
from copy import deepcopy
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]
   
R = len(grid)
C = len(grid[0])
items_pos = defaultdict(set)
items = set()

sx, sy = None, None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i == 0 and grid[i][j] == '.':
            sx, sy = i, j
        elif grid[i][j] not in ('.', '#', '~'):
            items_pos[grid[i][j]].add((i, j))
            items.add(grid[i][j])
            
all_points = [(sx, sy)] 
herb_info = []

for h_type in sorted(items):
    for pos in items_pos[h_type]:
        herb_info.append((h_type, pos))
        all_points.append(pos)

num_points = len(all_points)
dist_matrix = [[float('inf')] * num_points for _ in range(num_points)]
  
def bfs(sx, sy, ex, ey):
    queue = deque([(0, sx, sy)])
    seen = {(sx, sy)}
    while queue:
        step, x, y = queue.popleft()
        if (x, y) == (ex, ey):
            return step
        for nx, ny in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#" and grid[nx][ny] != "~":
                if (nx, ny) not in seen:
                    queue.append((step+1, nx, ny))
                    seen.add((nx, ny))
    return -1

for i in range(num_points):
    for j in range(i + 1, num_points):
        d = bfs(all_points[i][0], all_points[i][1], all_points[j][0], all_points[j][1])
        if d != -1:
            dist_matrix[i][j] = dist_matrix[j][i] = d
            
memo = {}
item_list = sorted(list(items))
type_to_idx = {name: i for i, name in enumerate(item_list)}
target_mask = (1 << len(items)) - 1

def solve(curr_idx, mask):
    state = (curr_idx, mask)
    if state in memo:
        return memo[state]
    
    if mask == target_mask:
        return dist_matrix[curr_idx][0]
    
    res = float('inf')
    
    for next_idx in range(1, num_points):
        h_type, h_pos = herb_info[next_idx - 1]
        type_bit = 1 << type_to_idx[h_type]
        
        if not (mask & type_bit):
            d = dist_matrix[curr_idx][next_idx]
            if d != float('inf'):
                res = min(res, d + solve(next_idx, mask | type_bit))
                
    memo[state] = res
    return res

print(solve(0, 0))