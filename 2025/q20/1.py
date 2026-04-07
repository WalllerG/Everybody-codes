with open('input.txt')as f:
    grid = [line for line in f.read().splitlines()]
trampolines = set()
for r, line in enumerate(grid):
    for c, char in enumerate(line):
        if char == 'T':
            trampolines.add((r, c))
ans = 0
for r, c in trampolines:
    neighbors = [(r, c-1), (r, c+1)]
    if (r + c) % 2 == 0:
        neighbors.append((r - 1, c))
    else:
        neighbors.append((r + 1, c))
    for nr, nc in neighbors:
        if (nr, nc) in trampolines:
            ans += 1
print(ans // 2)