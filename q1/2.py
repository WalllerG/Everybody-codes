with open("input.txt") as f:
    names, ops = f.read().split("\n\n")
names = names.split(",")
ops = ops.split(",")
cur = names[0]
index = 0
for op in ops:
    direction, num = op[0], int(op[1:])
    if direction == "R":
        index = (index + num) % len(names)
        cur = names[index]
    elif direction == "L":
        index = (index - num) % len(names)
        cur = names[index]
print(cur)

