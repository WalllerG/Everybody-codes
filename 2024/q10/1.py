with open('input.txt')as f:
   grid = [list(line) for line in f.read().splitlines()]

ans = ""

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '.':
                row = set(grid[i])
                col = []
                for x in range(len(grid)):
                    col.append(grid[x][j])
                col = set(col)
                intersect = col & row
                for inter in intersect:
                    if inter != ".":
                        ans += inter
                        break
    
print(ans)