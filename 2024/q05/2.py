from collections import defaultdict
with open('input.txt')as f:
    data = f.read().strip().splitlines()
    
cols = []
round = 0
shouts = defaultdict(int)

for i in range(4):
    col = []
    for line in data:
        line = line.split(' ')
        col.append(int(line[i]))
    cols.append(col)

while True:
    num = cols[round % len(cols)].pop(0)
    new_pos = (round + 1) % len(cols)
    indecies = [i for i in range(len(cols[new_pos]))] + [i for i in range(len(cols[new_pos]),0,-1)]
    cols[new_pos].insert(indecies[(num-1) % len(indecies)], num)
    round += 1
    number = int("".join(str(col[0]) for col in cols))
    shouts[number] += 1
    if shouts[number] == 2024:
        print(number * round)
        break