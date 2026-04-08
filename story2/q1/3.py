from collections import defaultdict
with open('input.txt')as f:
    grid, directions = f.read().split('\n\n')
grid = [list(line) for line in grid.splitlines()]
directions = directions.splitlines()
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

def dp():
    memo = defaultdict(list)
    for i in range(6):
        for num in range(1, 21):
            wins = count_wins(num, directions[i])
            score = wins if wins > 0 else 0
            memo[i].append((score, num))
    return memo

table = dp()
lists = [table[i] for i in range(6)]

best_max = -1
best_min = float('inf')

def backtrack(index, used, current_sum):
    global best_max, best_min

    if index == len(lists):
        if current_sum > best_max:
            best_max = current_sum
        if current_sum < best_min:
            best_min = current_sum
        return

    for score, num in lists[index]:
        if num not in used:
            used.add(num)
            backtrack(index + 1, used, current_sum + score)
            used.remove(num)

backtrack(0, set(), 0)
print(best_min, best_max)