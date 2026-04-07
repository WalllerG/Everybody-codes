import heapq
with open('input.txt')as f:
    data = f.read().splitlines()
S = (0, 0)
walls = {}
for line in data:
    x, y, height = list(map(int, line.split(',')))
    walls[x] = (y-1, y + height)
r = max(walls.keys())
c = max(walls.values(), key=lambda x:x[1])[1]+1
possible = [(88, y) for y in range(walls[88][0], walls[88][1])]
def bfs(target):
    queue = [(0, 0, 0)] 
    seen = {(0, 0): 0}
    while queue:
        flaps, x, y = heapq.heappop(queue)
        if x == target:
            return flaps
        nx, ny = x + 1, y + 1
        if nx <= target:
            if nx not in walls or (walls[nx][0] < ny < walls[nx][1]):
                new_flaps = flaps + 1
                if (nx, ny) not in seen or new_flaps < seen[(nx, ny)]:
                    seen[(nx, ny)] = new_flaps
                    heapq.heappush(queue, (new_flaps, nx, ny))
        nx, ny = x + 1, y - 1
        if nx <= target:
            if nx not in walls or (walls[nx][0] < ny < walls[nx][1]):
                new_flaps = flaps # No cost for falling
                if (nx, ny) not in seen or new_flaps < seen[(nx, ny)]:
                    seen[(nx, ny)] = new_flaps
                    heapq.heappush(queue, (new_flaps, nx, ny))
    return -1
print(bfs(88))