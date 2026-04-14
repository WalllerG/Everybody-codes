from collections import defaultdict
with open('input.txt')as f:
    grid = [list(line) for line in f.read().splitlines()][:-1]

segments = {'A':1,'B':2, 'C':3}
a = (1,1)
b = (1,2)
c = (1,3)
c_range = defaultdict(list)
b_range = defaultdict(list)
a_range = defaultdict(list)
targets = []
ans = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'T':
            targets.append((j, 4 - i))

def get_range():
        for i in range(1,11):
            sx, sy = c[0] + 2 * i, c[1] + i
            while sy > 1:
                sx, sy = sx + 1, sy -1
                c_range[i].append((sx, sy))
        for i in range(1,11):
            sx, sy = b[0] + 2 * i, b[1] + i
            while sy > 1:
                sx, sy = sx + 1, sy - 1
                b_range[i].append((sx, sy))
        for i in range(1,11):
            sx, sy = a[0] + 2 * i, a[1] + i
            while sy > 1:
                sx, sy = sx + 1, sy -1
                a_range[i].append((sx, sy))
    
get_range()
    
for t in targets:
    for power, vals in c_range.items():
        if t in vals:
            ans += power * 3
            break
    else:
        for power, vals in b_range.items():
            if t in vals:

                ans += power * 2
                break
        else:
            for power, vals in a_range.items():
                if t in vals:
    
                    ans += power * 1
                    break
print(ans)