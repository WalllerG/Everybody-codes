import re
with open('input.txt')as f:
    data = f.read().splitlines()

dies = {}

for line in data:
    info = re.findall(r"-?\d+", line)
    id, faces, seed = int(info[0]), list(map(int, info[1:-1])), int(info[-1])
    dies[id] = [faces, seed, 0, seed]

print(dies)
total = 0
roll_num = 0

while True:
    if total >= 10000:
        print(roll_num)
        break
    roll_num += 1
    for die, vals in dies.items():
        seed = vals[-1]
        cur = vals[1]
        spin = roll_num * cur
        cur += spin
        cur %= seed
        cur += 1 + roll_num + seed
        new_index = (vals[2] + spin) % len(vals[0])
        total += vals[0][new_index]
        dies[die][2] = new_index
        dies[die][1] = cur
