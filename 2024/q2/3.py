from collections import Counter, defaultdict
with open('input.txt')as f:
    words, grid = f.read().split('\n\n')

words = words.split(':')[1].split(',')
ans = 0
grid = [list(line)for line in grid.splitlines()]
cols = list(zip(*grid))
counts = [[[c, 0] for c in r] for r in grid]
    
for i in range(len(grid)):
    op_grid = "".join(grid[i])
    left_to_right = op_grid * 2
    for w in words:
        if w in left_to_right[::-1]:
            for j in range(len(left_to_right)-len(w)+1):
                if left_to_right[::-1][j:j+len(w)] == w:
                    for k in range(j,j+len(w)):
                        counts[i][::-1][k % len(op_grid)][1] += 1
                        
    wrap = op_grid * 2
    for w in words:
        if w in wrap:
            for j in range(len(wrap)-len(w)+1):
                if wrap[j:j+len(w)] == w:
                    for k in range(j,j+len(w)):
                        counts[i][k % len(op_grid)][1] += 1

for i, col in enumerate(cols):
    col = "".join(col)
    for w in words:
        if w in col:
            for j in range(len(col)-len(w)+1):
                if col[j:j+len(w)] == w:
                    for k in range(j,j+len(w)):
                        counts[k][i][1] += 1
        if w in col[::-1]:
            for j in range(len(col)-len(w)+1):
                if col[::-1][j:j+len(w)] == w:
                    for k in range(j,j+len(w)):
                        counts[::-1][k][i][1] += 1

for i in range(len(counts)):
    for j in range(len(counts[i])):
        if counts[i][j][1] > 0:
            ans += 1

print(ans)