with open("input.txt") as f:
    names, ops = f.read().split("\n\n")
names = names.split(",")
ops = ops.split(",")
for op in ops:
    direction = op[0]
    num = int(op[1:])
    if direction == "R":
        target_index = num % len(names)
    else:
        target_index = (-num) % len(names)
    names[0], names[target_index] = names[target_index], names[0]
print(names[0])
