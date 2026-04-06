import copy
with open('input.txt') as f:
    data = f.read().splitlines()
grid = [list(line) for line in data]
actives = {(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == "#"}
inactives = {(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == "."}
ans = 0
for _ in range(2025):
    new_a = set()
    new_ia = set()
    count = 0
    for x, y in actives:
        in_count = 0
        a_count = 0
        for nx, ny in [(x-1, y-1),(x-1, y+1),(x+1, y-1),(x+1, y+1)]:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if(nx, ny) in actives:
                    a_count += 1
                else:
                    in_count += 1
        if a_count % 2 != 0:
            new_a.add((x, y))
        else:
            new_ia.add((x, y))
    for x, y in inactives:
        in_count = 0
        a_count = 0
        for nx, ny in [(x-1, y-1),(x-1, y+1),(x+1, y-1),(x+1, y+1)]:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if(nx, ny) in actives:
                    a_count += 1
                else:
                    in_count += 1
        if a_count % 2 != 0:
            new_ia.add((x, y))
        else:
            new_a.add((x, y))
    ans += len(new_a)
    actives = new_a
    inactives = new_ia
print(ans)