with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()]

ans = 0
layer = set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            layer.add((i, j))

while True:
    if len(layer) == 0:
        print(ans)
        break
    ans += len(layer)
    new_layer = set()
    for x, y in layer:
        for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if (nx, ny) not in layer:
                break
        else:
            new_layer.add((x, y))
    layer = new_layer