import re
with open('input.txt')as f:
    data, sequence = f.read().split('\n\n')

sequence = list(sequence)
FINISH = len(sequence)
queue = []
finish_order = []

for line in data.splitlines():
    info = re.findall(r"-?\d+", line)
    id, faces, seed = int(info[0]), list(map(int, info[1:-1])), int(info[-1])
    queue.append((id, faces, seed, 0, seed, 0, 1))

while True:
    if len(finish_order) == 9:
        print(",".join(finish_order))
        break
    while queue:
        id, faces, pulse, die_index, seed, seq_index, roll_num = queue.pop(0)
        spin = roll_num * pulse
        pulse += spin
        pulse %= seed
        pulse += 1 + roll_num + seed
        new_index = (die_index + spin) % len(faces)
        if faces[new_index] == int(sequence[seq_index]):
            seq_index += 1
        if seq_index == FINISH:
            finish_order.append(str(id))
            continue
        else:
            queue.append((id, faces, pulse, new_index, seed, seq_index, roll_num+1))
