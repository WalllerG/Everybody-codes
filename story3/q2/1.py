with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]
S = ()
bone = ()
waves = set()
seqs = [(-1,0),(0,1),(1,0),(0,-1)]
index = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            S = (i, j)
        if grid[i][j] == '#':
            bone = (i, j)
cur = S
ans = 0
while True:
    x, y = cur
    if (x, y) == bone:
        print(ans)
        break
    dx, dy = seqs[index]
    nx, ny = x + dx, y + dy
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
        if (nx, ny) in waves:
            index = (index + 1) % 4
            continue
        index = (index + 1) % 4
        waves.add((x, y))
        cur = (nx, ny)
        ans += 1