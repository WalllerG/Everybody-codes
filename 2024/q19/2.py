with open('input.txt')as f:
    key, grid = f.read().split('\n\n')
    
key *= 1000
grid = [list(line) for line in grid.splitlines()]
R = len(grid)
C = len(grid[0])
round = 0
rotation_points = [(i, j) for i in range(R) for j in range(C) if i > 0 and i < R - 1 and j > 0 and j < C - 1]
for i in range(100):
    round = 0
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
        round += 1
        if round == len(rotation_points):
            break
    
for r in grid:
    print("".join(r))