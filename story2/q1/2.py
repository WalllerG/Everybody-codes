with open('input.txt')as f:
    grid, directions = f.read().split('\n\n')
grid = [list(line) for line in grid.splitlines()]
def count_wins(slot, line):
    cur = (0, (slot-1) * 2)
    for char in line:
        if cur[0] == len(grid)-1:
            cur = (cur[0], cur[1]-1) if char == 'L' else (cur[0], cur[1]+1)
            break
        if char == 'R':
            if cur[1] + 1 >= len(grid[0]):
                cur = (cur[0]+1, cur[1]-1)
                if grid[cur[0]][cur[1]] == "*":
                    continue
                try:
                    while grid[cur[0]][cur[1]] != '*':
                        cur = (cur[0]+1, cur[1])
                    continue
                except:
                    continue
            else:
                cur = (cur[0]+1, cur[1]+1)
                if grid[cur[0]][cur[1]] == '*':
                    continue
                try:
                    while grid[cur[0]][cur[1]] != '*':
                        cur = (cur[0]+1, cur[1])
                    continue
                except:
                    continue
        else:
            if cur[1] - 1 < 0:
                cur = (cur[0]+1, cur[1]+1)
                if grid[cur[0]][cur[1]] == '*':
                    continue
                try:
                    while grid[cur[0]][cur[1]] != '*':
                        cur = (cur[0]+1, cur[1])
                    continue
                except:
                    continue
            else:
                cur = (cur[0]+1, cur[1]-1)
                if grid[cur[0]][cur[1]] == '*':
                    continue
                try:
                    while grid[cur[0]][cur[1]] != '*':
                        cur = (cur[0]+1, cur[1])
                    continue
                except:
                    continue
    return ((cur[1] // 2 + 1) * 2 - slot)
ans = 0
for rule in directions.splitlines():
    local_max = 0
    for j in range(1, len(grid)+1):
        try:
            wins = count_wins(j ,rule)
            local_max = max(local_max, wins)
        except:
            continue
    ans += local_max
print(ans)
