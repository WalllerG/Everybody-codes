with open('input.txt')as f:
    key, grid = f.read().split('\n\n')
    
key *= 10000000
grid = [list(line) for line in grid.splitlines()]
rotation_points = [(1, c) for c in range(1, len(grid[0])-1)]

for index, k in enumerate(key):
    if k == 'R':
        x, y = rotation_points[index % len(rotation_points)]
        flatten = [grid[i][j] for i, j in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)]]
        rotated = flatten[-1:] + flatten[:-1]
        for (nx, ny), letter in zip([(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)], rotated):
            grid[nx][ny] = letter
    if k == "L":
        x, y = rotation_points[index % len(rotation_points)]
        flatten = [grid[i][j] for i, j in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)]]
        rotated = flatten[1:] + flatten[:1]
        for (nx, ny), letter in zip([(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1)], rotated):
            grid[nx][ny] = letter
    if grid[1][0] == '>' and grid[1][len(grid[1])-1] == '<':
        print("".join(grid[1][1:-1]))
        break