with open('input.txt')as f:
    data = f.read().splitlines()
grid = [list(line) for line in data]
moves = {(10, 10)}
queue = [(10, 10, 0)]
while queue:
    x, y, move = queue.pop(0)
    for nx, ny in [(x-2, y-1),(x-2, y+1),(x-1, y-2),(x-1, y+2),(x+2, y-1),(x+2, y+1),(x+1, y-2),(x+1, y+2)]:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in moves:
            if move + 1 < 5:
                moves.add((nx, ny))
                queue.append((nx, ny, move+1))
ans = 0
for x, y in moves:
    if grid[x][y] == "S":
        ans += 1
print(ans)