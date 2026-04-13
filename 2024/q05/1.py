with open('input.txt')as f:
    data = f.read().strip().splitlines()
    
cols = []
round = 0
for i in range(4):
    col = []
    for line in data:
        line = line.split(' ')
        col.append(int(line[i]))
    cols.append(col)

while round < 10:
    num = cols[round % len(cols)].pop(0)
    new_pos = (round + 1) % len(cols)
    cols[new_pos].insert(num-1, num)
    round += 1

for col in cols:
    print(col[0])